import sys

def write_line_to_file(file_path, keywords=[], values=[], line_to_add=None):
    just_write_line = False

    if not line_to_add:
        line_to_add = " ".join(keywords) + ','  # separate each keyword with a space. This will be the header for the new line
        line_to_add += ','.join(values) + '\n'  # if values are given, then write the values to the line too
    else:
        just_write_line = True

    try:
        with open(file_path, "r+") as file:  # opening the file
            lines = file.readlines()

            if just_write_line:
                stop_loop = False
                for i in range(len(lines)):
                    if stop_loop:
                        break
                    for keyword in keywords:
                        if keyword in lines[i]:
                            lines[i] = line_to_add  # as long as one of the keywords is there, that is the correct line
                            stop_loop = True
                            break

            else:
                # getting the table headers of each line
                headers = [line.split(',')[0] for line in lines]  # the header will be before the first ','
                
                # making sure the order of the keywords in the header do not matter
                keywords = set(keywords)

                # checking if there is a header with only those flags already
                for i in range(len(lines)):
                    header_keywords = set(headers[i].split())
                    
                    # comparing two sets, so that order doesn't matter
                    if header_keywords == keywords:  # if line i contains all keywords passed to this script
                        lines[i] = line_to_add  # erase all values on that line
                        break  # stop iterating because that line has been found
                
                else:  # if there was no line starting with the header (the loop didn't break)
                    lines.append(line_to_add)

            file.seek(0)
            file.truncate()  # clearing the file and rewriting the contents
            file.writelines(lines)  # rewrite the file.

    except FileNotFoundError: # if the file was not found, create a new one and add the execution times to it
        with open(file_path, "w") as file:
            file.write(line_to_add)

