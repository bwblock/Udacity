import sys
import logging

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def reducer():
    '''
    Write a reducer that will compute the busiest date and time (that is, the 
    date and time with the most entries) for each turnstile unit. Ties should 
    be broken in favor of datetimes that are later on in the month of May. You 
    may assume that the contents of the reducer will be sorted so that all entries 
    corresponding to a given UNIT will be grouped together.
    
    The reducer should print its output with the UNIT name, the datetime (which 
    is the DATEn followed by the TIMEn column, separated by a single space), and 
    the number of entries at this datetime, separated by tabs.

    For example, the output of the reducer should look like this:
    R001    2011-05-11 17:00:00	   31213.0
    R002	2011-05-12 21:00:00	   4295.0
    R003	2011-05-05 12:00:00	   995.0
    R004	2011-05-12 12:00:00	   2318.0
    R005	2011-05-10 12:00:00	   2705.0
    R006	2011-05-25 12:00:00	   2784.0
    R007	2011-05-10 12:00:00	   1763.0
    R008	2011-05-12 12:00:00	   1724.0
    R009	2011-05-05 12:00:00	   1230.0
    R010	2011-05-09 18:00:00	   30916.0
    ...
    ...

    Since you are printing the output of your program, printing a debug 
    statement will interfere with the operation of the grader. Instead, 
    use the logging module, which we've configured to log to a file printed 
    when you click "Test Run". For example:
    logging.info("My debugging message")
    Note that, unlike print, logging.info will take only a single argument.
    So logging.info("my message") will work, but logging.info("my","message") will not.
    '''


    max_riders = 0
    old_key = None
    datetime = ''

    for line in sys.stdin:
        data = line.strip().split("\t")
#        logging.info(data)
        if len(data) < 3:
          logging.info('loop')
          continue
      
      
        
        this_key = data[0]
        count = float(data[1])
        
        if old_key and old_key != this_key:

          out = "{0}\t{1}\t{2}".format(old_key, datetime, max_riders)
          print out
          logging.info(out)
          datetime = ''
          max_riders = 0


        old_key = this_key
        if count >= max_riders:
           max_riders = count
           datetime = data[2] + ' ' + data[3]

        
    if old_key != None:
      print"{0}\t{1}\t{2}".format(old_key, datetime, max_riders)
reducer()
