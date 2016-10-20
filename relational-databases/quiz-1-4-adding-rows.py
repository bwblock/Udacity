#
# Insert a newborn baby opossum into the animals table and verify that it's been added.
# To do this, fill in the rest of SELECT_QUERY and INSERT_QUERY.
# 
# SELECT_QUERY should find the names and birthdates of all opossums.
# 
# INSERT_QUERY should add a new opossum to the table, whose birthdate is today.
# (Or you can choose any other date you like.)
#
# The animals table has columns (name, species, birthdate) for each individual.
#

SELECT_QUERY = "select name, birthdate from animals where species = 'opossum';"



INSERT_QUERY = "insert into animals (name, species, birthdate) values ('Freddy', 'opossum','2016-10-18');"



The basic syntax for the insert statement:

insert into table ( column1, column2, ... ) values ( val1, val2, ... );

If the values are in the same order as the table's columns (starting with the first column), you don't have to specify the columns in the insert statement:

insert into table values ( val1, val2, ... );

For instance, if a table has three columns (a, b, c) and you want to insert into a and b, you can leave off the column names from the insert statement. But if you want to insert into b and c, or a and c, you have to specify the columns.

A single insert statement can only insert into a single table. (Contrast this with the select statement, which can pull data from several tables using a join.)
