import csv


def write_to_csv(file_handle, objects):
    fieldnames = ['file_name', 'path', 'line_count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for object in objects:   
        file_name = object.file_name()
        path = object.path()
        line_count = object.line_count()
        writer.writerow({'file_name': file_name, 'path': path, 'line_count': line_count})