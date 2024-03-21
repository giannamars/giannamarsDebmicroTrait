# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os
import sys
import uuid

import numpy as np
#from sklearn.preprocessing import StandardScaler
#from sklearn.decomposition import PCA
import giannamarsDebmicroTrait.utils.helpers as h

from datetime import datetime

from installed_clients.WorkspaceClient import Workspace as workspaceService
from installed_clients.DataFileUtilClient import DataFileUtil as DFUClient
from installed_clients.KBaseReportClient import KBaseReport
#END_HEADER


class giannamarsDebmicroTrait:
    '''
    Module Name:
    giannamarsDebmicroTrait

    Module Description:
    A KBase module: giannamarsDebmicroTrait
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/giannamars/giannamarsDebmicroTrait.git"
    GIT_COMMIT_HASH = "625f1a7428cda4574e85a718b4620c8d5dd02ae9"

    #BEGIN_CLASS_HEADER
    def now_ISO(self):
        now_timestamp = datetime.now()
        now_secs_from_epoch = (now_timestamp - datetime(1970,1,1)).total_seconds()
        now_timestamp_in_iso = datetime.fromtimestamp(int(now_secs_from_epoch)).strftime('%Y-%m-%d_%T')
        return now_timestamp_in_iso

    def log(self, target, message):
        message = '['+self.now_ISO()+'] '+message
        if target is not None:
            target.append(message)
        print(message)
        sys.stdout.flush()
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.workspaceURL = config['workspace-url']
        self.shockURL = config['shock-url']
        self.callbackURL = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        self.scratch = os.path.abspath(config['scratch'])
        if not os.path.exists(self.scratch):
            os.makedirs(self.scratch)
        #END_CONSTRUCTOR
        pass


    def run_giannamarsDebmicroTrait(self, ctx, params):
        """
        This example function accepts any number of parameters and returns results in a KBaseReport
        :param params: instance of mapping from String to unspecified object
        :returns: instance of type "ReportResults" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN run_giannamarsDebmicroTrait
       
        console = []
        invalid_msgs = []
        objects_created = []
        file_links = []
        self.log(console, 'Running giannamarsDebmicroTrait()')
        report = ''
        timestamp = int((datetime.utcnow() - datetime.utcfromtimestamp(0)).total_seconds() * 1000)
        output_dir = os.path.join(self.scratch, 'output_' + str(timestamp))
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        SERVICE_VER = 'dev'  # DEBUG
        token = ctx['token']
        try:
            wsClient = workspaceService(self.workspaceURL, token=token)
        except Exception as e:
            raise ValueError("unable to instantiate wsClient. "+str(e))
        try:
            dfuClient = DFUClient(self.callbackURL, token=token, service_ver=SERVICE_VER)
        except Exception as e:
            raise ValueError("unable to instantiate dfuClient. "+str(e))
        

        html_output_dir = os.path.join(output_dir, 'output_html.' + str(timestamp))
        if not os.path.exists(html_output_dir):
            os.makedirs(html_output_dir)
        
        # Load precomputed data
        substrate_thermodynamics_data = os.path.join('/kb/module/data', 'substrate_thermodynamic_traits.csv')
        substrate_thermodynamics = h.plot_substrate_thermodynamic_traits(params, substrate_thermodynamics_data, html_output_dir)
       
        # Generate dummy table data 
        data_array = np.random.rand(3, 39)
        headers = ['Header ' + str(i) for i in range(1, 40)]  # Sample headers

        api_results = {
            "png1": substrate_thermodynamics['name'],
            "header": headers,
            "data": data_array
        }


        html_report = h.html_add_batch_summary(params, api_results, html_output_dir)

        try:
            html_upload_ret = dfuClient.file_to_shock({'file_path': html_report['path'],
                                                'make_handle': 0,
                                                'pack': 'zip'})
        except:
            raise ValueError('error uploading html file to shock')
        
        try:
            png_upload_ret = dfuClient.file_to_shock({'file_path': substrate_thermodynamics['path'],
                                                'make_handle': 0})
        except:
            raise ValueError('error uploading png file to shock')

    
        reportName = 'view_tree_report_' + str(uuid.uuid4())

        reportObj = {'objects_created': [],
                     'direct_html_link_index': 0,
                     'file_links': [],
                     'html_links': [],
                     'workspace_name': params['workspace_name'],
                     'report_object_name': reportName
                     }
        
        reportObj['html_links'] = [{'shock_id': html_upload_ret['shock_id'],
                                    'name': html_report['name'],
                                    'label': 'test' + ' HTML'
                                    }
                                   ]
        
        reportObj['file_links'] = [{'shock_id': png_upload_ret['shock_id'],
                                    'name': 'pan_circle_plot.png',
                                    'label': 'test plot'
                                    }
                                   ]
        
        reportClient = KBaseReport(self.callbackURL, token=ctx['token'], service_ver=SERVICE_VER)
        report_info = reportClient.create_extended_report(reportObj)

        self.log(console, "BUILDING RETURN OBJECT")
        output = {'report_name': report_info['name'],
                  'report_ref': report_info['ref']
                  }

        self.log(console, "giannamarsDebmicroTrait() DONE")
        #END run_giannamarsDebmicroTrait

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method run_giannamarsDebmicroTrait return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
