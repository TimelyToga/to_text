from bs4 import BeautifulSoup
import sys
import re



OUTPUT_FILE = "output.txt"

if(len(sys.argv) == 2):
	input_file = sys.argv[1]
elif len(sys.argv == 3):
	input_file = sys.argv[1]
	OUTPUT_FILE = sys.argv[2]
else:
	print "\n\nto_text.py will convert your Evernote .enex export into a plain text file.\nThis file's usuage is as follows:\n\npython to_text.py <input_xml_filename> [OPTIONAL]<output_filename>\n\n"
	sys.exit()

print "Reading input file..."

with open(input_file, 'r') as f:
	read_file = f.read()

print "Converting file..."

soup = BeautifulSoup(read_file)
journal_entries = soup.find_all('note')
notes = []

print "Cleaning file text..."

for entry in journal_entries:
	dirty = entry.content.text
	clean = re.sub("<.*?>", "", dirty)
	clean = clean.replace('\n', ' ').replace('\r', '')
	notes.append(clean)

all_text = "\n\n".join(notes)
all_text = all_text
all_text = all_text.encode('utf8')

print "Writing output..."

with open(OUTPUT_FILE, 'w') as f:
	f.write(all_text)

print "Finished\n"