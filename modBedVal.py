import sys
import os
import csv
#import operator

def main(argv):
    if len(argv) < 2:
        sys.stderr.write("Usage: %s bed_file\n" % argv[0])
        return 1
    if not os.path.isfile(argv[1]):
        sys.stderr.write('Error: bed_file %r was not found!\n' % argv[1])
        return 1

    #ofile = open('/home/xc406/data/bed_test/' +  shortname + '_o', 'w')
    #writer = csv.writer(ofile, delimiter = '\t')    
    infile = sys.argv[1]

    (path,fname) = os.path.split(infile)
    (shortname, extension) = os.path.splitext(fname)
    ifile = open(infile,'rU')
    reader = csv.reader(ifile, delimiter = '\t')
    
    ofile = open('/home/xc406/data/' +  shortname + '1.bed', 'w')
    writer = csv.writer(ofile, delimiter = '\t')


    for row in reader:
	row[4] = 1
	writer.writerows([row])
	#pline = row
	#pstart = row[3]
        #pstop = row[4]
        #pchr = row[1]            

    ofile.close()

if __name__=='__main__':
    sys.exit(main(sys.argv))


