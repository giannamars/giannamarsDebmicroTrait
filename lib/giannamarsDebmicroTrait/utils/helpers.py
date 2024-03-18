import os

def html_header():
    report = []
    report.append("<style>* {font-family: sans-serif; font-size: 14px}</style>")

    return report


def html_add_ontology_summary(params, ontology, api_results, output_directory):

    output_file = os.path.join(output_directory, "add_ontology_summary.html")

    # Make report directory and copy over files
    report = html_header()

    report.append(f'<h3>Import Annotations Summary</h3>')


    # Write to file
    with open(output_file, 'w') as f:
        for line in report:
            f.write(line + "\n")

    return {'path': output_directory,
            'name': os.path.basename(output_file),
            'description': 'HTML report for import_annotations app'}

