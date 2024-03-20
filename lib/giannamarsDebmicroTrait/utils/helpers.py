import os

def html_header():
    report = []
    report.append("<style>* {font-family: sans-serif; font-size: 14px}</style>")

    return report


def html_add_batch_summary(params, html_output_dir):

    #output_file = os.path.join(output_directory, "add_ontology_summary.html")
    html_file = 'test' + '.html'
    output_html_file_path = os.path.join(html_output_dir, html_file)


    img_dpi = 300
    img_units = "in"
    img_pix_width = 1200
    img_in_width = round(float(img_pix_width) / float(img_dpi), 1)
    img_html_width = img_pix_width // 2

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
    html_report_lines.append('.tab-button {')  # Added class for tab buttons
    html_report_lines.append('  background-color: white;')  # Set background color to white
    html_report_lines.append('}')
    html_report_lines.append('</style>')
    html_report_lines.append('</head>')
    html_report_lines.append('<body>')

    # Tab navigation
    html_report_lines.append('<div>')
    html_report_lines.append('<button class="tab-button" onclick="showTab(0)">Image 1</button>')  # Added class for tab buttons
    html_report_lines.append('<button class="tab-button" onclick="showTab(1)">Image 2</button>')  # Added class for tab buttons
    html_report_lines.append('<button class="tab-button" onclick="showTab(2)">Background</button>')  # Added class for tab buttons
    html_report_lines.append('<button class="tab-button" onclick="showTab(3)">Table</button>') 
    html_report_lines.append('</div>')

    # Tab content
    html_report_lines.append('<div id="tabContent">')
    html_report_lines.append('<div class="tab active">')
    html_report_lines.append('<div><h2>Image 1</h2></div>')  # Header for Image 1
   # html_report_lines.append('<img width="{0}" src="{1}">'.format(img_html_width, png_file))
    html_report_lines.append('</div>')
    html_report_lines.append('<div class="tab">')
    html_report_lines.append('<div><h2>Image 2</h2></div>')  # Header for Image 1
    #html_report_lines.append('<img width="{0}" src="{1}">'.format(img_html_width, png_file))
    html_report_lines.append('</div>')
    html_report_lines.append('<div class="tab">')
    html_report_lines.append('<div><h2>Background</h2></div>') 
    html_report_lines.append('<div style="width: 100%; height: 100vh; background-color: black;"></div>')
    html_report_lines.append('</div>')
    html_report_lines.append('<div class="tab">')
    html_report_lines.append('<div><h2>Table</h2></div>')  # Header for the table tab
    # Table content
    html_report_lines.append('<table border="1">')  # Basic table with borders
    # Table header row
    html_report_lines.append('<tr>')
   # for header in headers:
   #     html_report_lines.append('<th>{}</th>'.format(header))
   # html_report_lines.append('</tr>')
    # Data rows
   # for row in data_array:
   #     html_report_lines.append('<tr>')
   #     for cell in row:
   #         html_report_lines.append('<td>{}</td>'.format(cell))
   #     html_report_lines.append('</tr>')
    html_report_lines.append('</table>')
    html_report_lines.append('</div>')
    html_report_lines.append('</div>')

    # Text below the table
    html_report_lines.append('<div>')
    html_report_lines.append('<p>This is a line of text below the table.</p>')
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


    return {'path': output_html_file_path,
            'name': os.path.basename(output_html_file_path),
            'description': 'HTML report for batch mode simulations'}


