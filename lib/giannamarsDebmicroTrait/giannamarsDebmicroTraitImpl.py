# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os
import sys
import uuid

import matplotlib.pyplot as pyplot
#import seaborn as sns
#import pandas as pd
#import numpy as np
#from sklearn.preprocessing import StandardScaler
#from sklearn.decomposition import PCA

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
    GIT_COMMIT_HASH = "9f0f6f299787c0f2bcf3e140790999a5e4c934d7"

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
        

        img_dpi = 300
        img_units = "in"
        img_pix_width = 1200
        img_in_width = round(float(img_pix_width) / float(img_dpi), 1)
        img_html_width = img_pix_width // 2


        fig = pyplot.figure()
        fig.set_size_inches(img_in_width, img_in_width)
        fig, ax = pyplot.subplots(nrows=1, ncols=1)  
        ax.plot([0,1,2], [10,20,3])
       
        
        html_output_dir = os.path.join(output_dir, 'output_html.' + str(timestamp))
        if not os.path.exists(html_output_dir):
            os.makedirs(html_output_dir)
        html_file = 'test' + '.html'
        output_html_file_path = os.path.join(html_output_dir, html_file)

        png_file = 'pangenome_circle.png'
        output_png_file_path = os.path.join(html_output_dir, png_file)
        fig.savefig(output_png_file_path, dpi=img_dpi)

        # make html
        html_report_lines = []
        html_report_lines += ['<html>']
        html_report_lines += ['<head><title>KBase Tree: ' + 'intree_name' + '</title></head>']
        html_report_lines += ['<body bgcolor="black">']
        html_report_lines += ['<img width=' + str(img_html_width) + ' src="' + png_file + '">']
        html_report_lines += ['</body>']
        html_report_lines += ['</html>']

        html_report_str = "\n".join(html_report_lines)


        # Make HTML
        intree_name = 'intreename'

        html_report_lines = []
        html_report_lines.append('<html>')
        html_report_lines.append('<head>')
        html_report_lines.append('<title>KBase Tree: {0}</title>'.format(intree_name))
        html_report_lines.append('<style>')
        html_report_lines.append('.tab {')
        html_report_lines.append('  display: none;')
        html_report_lines.append('}')
        html_report_lines.append('.active {')
        html_report_lines.append('  display: block;')
        html_report_lines.append('}')
        html_report_lines.append('</style>')
        html_report_lines.append('</head>')
        html_report_lines.append('<body>')

        # Tab navigation
        html_report_lines.append('<div>')
        html_report_lines.append('<button onclick="showTab(0)">Image</button>')
        html_report_lines.append('<button onclick="showTab(1)">Background</button>')
        html_report_lines.append('</div>')

        # Tab content
        html_report_lines.append('<div id="tabContent">')
        html_report_lines.append('<div class="tab active">')
        html_report_lines.append('<img width="{0}" src="{1}">'.format(img_html_width, png_file))
        html_report_lines.append('</div>')
        html_report_lines.append('<div class="tab">')
        html_report_lines.append('<div style="width: 100%; height: 100vh; background-color: black;"></div>')
        html_report_lines.append('</div>')
        html_report_lines.append('</div>')

        # JavaScript for tab switching
        html_report_lines.append('<script>')
        html_report_lines.append('function showTab(index) {')
        html_report_lines.append('  var tabs = document.getElementsByClassName("tab");')
        html_report_lines.append('  for (var i = 0; i < tabs.length; i++) {')
        html_report_lines.append('    tabs[i].classList.remove("active");')
        html_report_lines.append('  }')
        html_report_lines.append('  tabs[index].classList.add("active");')
        html_report_lines.append('}')
        html_report_lines.append('</script>')

        html_report_lines.append('</body>')
        html_report_lines.append('</html>')

        html_report_str = "\n".join(html_report_lines)
        
        with open(output_html_file_path, 'w') as html_handle:
            html_handle.write(html_report_str)

        try:
            html_upload_ret = dfuClient.file_to_shock({'file_path': html_output_dir,
                                                 'make_handle': 0,
                                                 'pack': 'zip'})
        except:
            raise ValueError('error uploading html file to shock')
        
        try:
            png_upload_ret = dfuClient.file_to_shock({'file_path': output_png_file_path,
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
                                    'name': html_file,
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
