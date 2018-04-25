http://www.thalesians.com/finance/index.php/Knowledge_Base/Databases/Kdb
https://pietrowski.info/2012/12/kdb-high-performance-column-oriented-designed-for-massive-datasets-database/
http://www.timestored.com/kdb-guides/
https://lifeisalist.wordpress.com/tag/kdb/

http://interviewquestions.emyreview.com/tag/kdb-q-interview-questions
https://eternallearningq.wordpress.com/
https://kx.com/

t1 : ([] name:`symbol$(); age:`int$())
t1 ,: (`Methuselah, 969)
t1 : flip[d1]
#save table to binary file
(`$":H:/myt1.dat") set t1
#load binary file to table
t2 : get (`$":H:/myt1.dat")
Q and k compile to the same byte code that is executed in the kdb+ byte interpreter
#un it on linux
/home/pbilokon/bin/rlwrap /home/pbilokon/q/l64/q
\t select from table;
#make one column out of 2
select contributor: "_" sv/: flip string(location;market) from SampleTable
#trim output
\c 25 150
#get columns 
col tabname
#connect to remote kdb
h : hopen `::8011
#upsert
upsert [`TestTable] (`EURUSD; 2009.02.10; 1.2874)
#save to a file
`:H:/somefile.dat set TestTable
#load
AnotherTestTable : get `:H:/somefile.dat
#delete
delete from `TestTable
#drop
delete TestTable from `.
#non-keyed table
TestTable : ([] sym:`symbol$(); date:`date$(); val:`float$())
#create keyd table
`sym`date xkey `TestTable
#turn back to nonkeyed
() xkey `TestTable
# remove duplicates
select by sym, date from TestTable
#copy of the list 
with the last element removed
(count l - 1)#l
#switch from k mode to q mode
\.
#shell commands
/command
#tables 
-are created out of lists
-created in memory
? verb generates random data
#hdb
holds data before today (on disk)
#Dictionaries 
are maps of lists to lists. 
#A table 
is a list of similar dicts(records).
!- map
d:`x`y!(`a;2)         / a dict is a map from a list to a list
f:(d;`x`y!(`b;3))     / a table is a list of dictionaries 
f:flip`x`y!(`a`b;2 3) / same table as flip of dict of lists
([]x:`a`b;y:2 3)      / a column notation for the same table 

#A keyed table 
is a dict whose key and value are both tables.

#To add records to a table:
t,:u / u is a record(dict) or a table
-Column names have to line up. 
-types have to match.

joins: (left+inner)*(fkey+adhoc)*(equi+asof)
Left joins subdivide into fkey and adhoc

lj - left join

/ conditional expression                                                       
$[cond;true;false]             / $[..;[..;..];[..;..]] for multiple expressions
$[cond;true;cond;true;..false]                                                 

q)) \   / abort 
q)) '   / signal
q)) :.. / return
#to evaluate use 
value()
value("select ", columnToBeSelected, " from TestTable")

#arguments to a script
name : .z.x 0;
surname : .z.x 1;
dob : .z.x 2;
#casting string to integer
"I"$dob
#appending to a list
L ,: "abc"
#send value to STDOUT
0N!result;
`t doesn't work on locals, whereas ,: does:
:t -assign to it

/ Dictionaries are combined using "upsert" semantics.
dict1,dict2
-dict has domain column and range column
table is a list of similar dictionaries (flipped)
`name xkey `e2 / creates a key.
0!t - removes key
#convert char to list
enlist x
-no operator presedence, only position pesedence

a%b     Divide        
a=b     Equal         
a>b     More          
a<b     Less          
a|b     Or (Max)      
a&b     And (Min)

x where x in y / 6 8 7 6 / This is a form of set intersection
distinct x where x in y

group zdup / returns a dictionary with the unique elements
/ of zdup in  the domain and their positions in the range 
/ 50 51 52 53 54!(0 9;1 8;2 7;3 6;4 5) 
type d

`name xkey `e

~  asks whether two entities have the same contents.
,  concatenates two lists.                          
_  drops elements of a list.                        
#  selects elements of a list.                      
?  finds the positions of elements of a list.       
?  is overloaded to generate random numbers.        
bin  supports binary search. 

evens: 2 * til 20   

There are three adverbs: each, eachleft and eachright.
x,'y / (each)
x,\: y / (each left)
x,/: y / (each right)	
/ Combine each left and each right to be a cross-product (cartesian product)
x,/:\:y
/ unary operator that undoes a level of nesting: "raze"            
raze x,/:\:y
reverse (1 2 3 4;"abc")      / reverses the two elements of this list:
/ returns ("abc";1 2 3 4)                                             
each[reverse](1 2 3 4;"abc") / reverses each list within this pair
/ returns (4 3 2 1;"cba")    
reverse each (1 2 3 4;"abc")


There are functional forms of Amend based on @ and Dot.

15 Rename, Rearrange

xcol  [p]rename    `a`b xcol sp 
xcols [p]rearrange `p`s xcols sp

The big table columns are mapped in and out on demand.

Lastly, we'll use ' (each-both) to join corresponding elements from two vectors of the same length (like zip from Python or Haskell):

q)1 2 3 ,' 10 20 30
1 10
2 20
3 30
#can be used as map on list
q)atomic: {[x; y] (x * x) + y * y}
q)atomic'[1 2 3; 10 20 30]
101 404 909
#sometimes it's called multivalent each

q)("car"; "far"; "mar") ,' "e"
"care"
"fare"
"mare"
q)

tbl:([]ids:10?`1;price:10?100.0)
#display row size
count -8!tbl
or
-22!x 

#table attributes
`s# sorted
`u# unique (hash table)
`p# partitioned (grouped)
`g# true index (dynamic attribute): enables constant time update and access for realtime tables
q)r:attr L
The result is a symbol atom and is one of `s`u`p`g` with 
` meaning no attributes are set on the argument.

#get used memory
.Q.w[] `used
#update
q)t: ([] f: 1000000 ? 1.0)
q)u: update g: 1000000 ? 5.0 from t

#very large databases
may be further partitioned using par.txt

#list 
is an ordered collection of atoms and other lists

#pos/neg
q)signum type enlist 42
1i

#dictionaries
-ordered collection  of key-value pairs 
equivalent to a hash table
xkey (!) primitive is used for list creation
extentions of lists
foundation of tables
key->value
-mapping of asimple list to simple list
#cols d
returns domain
#Reverse lookup with find
d?77
77-value
returns key
#removing entrie from dict
d2 _`z
#deleting multiple
`x`y _ d2

#A Table
is a collection of named colums implemented as a dictionary
q tablesa are column oriented
-type of the column is set by first insert
q)trade:([]time:();sym:();price:();size:())
q)trade:([]time:`time$();sym:`$();price:`float$();size:`int$())
q)trade:([]sym:(`a`b);price:(1 2))
#get metadata
show meta trade

#ForeignKeys
A foreign key defines a mapping from the rows of the table in which it is defined
to the rows of the table with the corresponding primary key.

Kdb+ has nouns, verbs, and adverbs. All data objects and functions are nouns.
Verbs enhance the readability by reducing the number of square brackets and
parentheses in expressions. Adverbs modify dyadic (2 arguments) functions and
verbs to produce n
ew, related verbs. The functions produced by adverbs are called
derived functions or derived verbs

each [reverse] (1 2 3; "abc") /Reverse-Each
'[reverse] ( 1 2 3; "abc")

q)x, \:y / each left, returns a list of each element
/ from x with all of y

q)x,/:y / each right, returns a list of all the x with
/ each element of y
q)x,/:\:y
q)1 _x 
q)-2_y 

Simple join
 Asof join
 Left join
 Union join

#Asof Join (aj)
It is the most powerful join which is used to get the value of a field in one table
asof the time in another table. Generally it is used to 
$ get the prevailing bid and ask at the time of each trade.

aj[joinColumns;tbl1;tbl2]
aj[`sym`time;trade;quote]

#Left Join(lj)
It’s a special case of aj where the second argument is a keyed table and the first
argument contains the columns of the right argument’s key.

table1 lj Keyed-table

#Union Join (uj)
It allows to create a union of two tables with distinct schemas. It is basically an
extension to the simple join ( , )

#functions
Atomic – Where the arguments are atomic and produce atomic results
 Aggregate – atom from list
 Uniform (list from list) – Extended the concept of atom as they apply to lists.
The count of the argument list equals the count of the result list.
 Other – if the function is not from the above category.

#all
q) all 4 5 0 -4 / Logical AND (numeric min), returns the minimum value
0b

q) 1b & 1b / And (Max)
1b
q) 1b|0b / Or (Min)

q)asc 1 3 5 7 -2 0 4 / Order list ascending, sorted list
/ in ascending order i
s returned


q)/attr - gives the attributes of data, which describe how it's sorted.
`s denotes fully sorted, `u denotes unique and `p and `g are used to
refer to lists with repetition, with `p standing for parted and `g for
grouped


q)(1 3 5) cut "abcdefghijkl" 

q)/distinct - Returns the distinct element of a list
q)distinct 1 2 3 2 3 4 5 2 1 3 

q)first 1 3 34 5 3

#get sort index
q)iasc 5 4 0 3 4 9
q)idesc 0 1 3 4
3 2 1 0

q)(2 4) in 1 2 3
10b

#datetime
q)value each {x!x}`.z.p`.z.P`.z.t`.z.T`.z.d`.z.D`.z.n`.z.z`.z.Z

q)/key - three different functions i.e. generate +ve integer number,
gives conte
nt of a directory or key of a table/dictionary.
q)key 9
0 1 2 3 4 5 6 7 8
q)key `:c:

q)f:key`:c:/q
q)f where f like "*.q"

q)key each ("abc";101b;1 2 3h;1 2 3;1 2 3j;1 2 3f)
`char`boolean`short`int`long`float

Given a positive integer, it acts like til:

q)key 10
0 1 2 3 4 5 6 7 8 9

#list of all types
q){key x$()}'[.Q.t where " "<>.Q.t]
`boolean`guid`byte`short`int`long`real`float`char`symbol`timestamp`month`date`datetime`timespan`minute`second`time

q)/fill - used with nulls. There are three functions for processing null
values.

q)/fills - fills in nulls with the previous not null value.

q)/null - return 1b if the atom is a null else 0b from the argument list
q)null 1 3 3 0N

q)/peach - Parallel each, allows process across slaves
q)foo peach list1 / function foo applied across the slaves named in
list1

q)/prev - returns the previous element i.e. pushes list forwards
q)prev 0 1 3 4 5 7
0N 0 1 3 4 5

q)/random - syntax - n?list, gives random sequences of ints and floats
q)9?5
0 0 4 0 3 2 2 0 1

q)/raze - Flattn a list of lists, removes a layer of indexing from a
list of lists. 

q)/read0 - Read in a text file
q)read0 `:c:/q/README.txt / gives the contents of *.txt file

q)/read1 - Read in a q data file
q)read1 `:c:/q/t1

q)`:c:/q/test12 set trade

q)/ssr - String search and replace
q)ssr["HelloWorld";"o";"O"]
"HellOWOrld"

q)24 60 60 sv 11 30 49
41449 / number of seconds elapsed in a day at 11:30:49

q)/trim - Eliminate string spaces

q)"|" vs "20150204|msft|20.45"
"20150204"
"msft"
"20.45"

#sorts table
q)`price xasc trade

q)/xcol - Renames columns of a table
q)`timeNew`symNew xcol trade


q)/xcols - Reorders the columns of a table,
q)`size`price xcols trade


q)`x xgroup ([]x:9 18 9 18 27 9 9;y:10 20 10 20 30 40 10)
x | y
--| -----------
9 | 10 10 40 10
18| 20 20
27| ,30


q)/xkey - Set key on table
q)`sym xkey trade

q)deltas 2 3 5 7 9
2 1 2 2 2


q)/maxs - takes scalar, list, dictionary or table and returns the
cumulative maximum of the source items.
q)maxs 1 2 4 3 9 13 2
1 2 4 4 9 13 13

q)1 2 3 4 3 1 except 1
2 3 4 3

q)/fill (^) - takes an atom as its first argument and a list(target) as
its second argument and return a list obtained by substituting the first
argument for every occurrence of null in target
q)42^ 9 18 0N 27 0N 36
9 18 42 27 42 36


update t set [a] [where c]


sym:asc`AIG`CITI`CSCO`IBM`MSFT;
ex:"NASDAQ"
dst:`$":c:/q/test/data/"; /database destination
@[dst;`sym;:;sym];
n:1000000;
trade:([]sym:n?`sym;time:10:30:00.0+til
n;price:n?3.3e;size:n?9;ex:n?ex);
quote:([]sym:n?`sym;time:10:30:00.0+til
n;bid:n?3.3e;ask:n?3.3e;bsize:n?9;asize:n?9;ex:n?ex);
{@[;`sym;`p#]`sym xasc x}each`trade`quote;
d:2014.08.07 2014.08.08 2014.08.09 2014.08.10 2014.08.11; /Date vector
can also be changed by the user
dt:{[d;t].[dst;(`$string d;t;`);:;value t]};
d dt/:\:`trade`quote;


Count the number of records (in millions) for a certain month
(select trade:1e-6*count i by date.dd from trade where
date.month=2014.08m) 


Daily High, Low, Open and Close for CSCO in a certain month
select high:max price,low:min price,open:first price,close:last price by
date.dd from trade where date.month=2014.08m,sym=`CSCO


Select the price range in hourly buckets
select range:max[price] – min price by date,sym,hour:time.hh from trade

select spread:avg bid-ask by date.dd from quote where
date.month=2014.08m, sym=`CSCO

Extract a 5 minute vwap for CSCO
select size wavg price by 5 xbar time.minute from trade where sym=`CSCO

 Extract 10 minute bars for CSCO
select high:max price,low:min price,close:last price by date,10 xbar
time.minute from trade where sym=`CSCO

Find the times when the price exceeds 100 basis points (100e-4) over
the last price for CSCO for a certain day
select time from trade where date=2014.08.11,sym=`CSCO,price>1.01*last
price

 Full Day Price and Volume for MSFT in 1 Minute Intervals for the last
date in the database
select last price,last size by time.minute from trade where date=last
date, sym=`MSFT

#Check if list is sorted
q)`s#L2
The sorted attribute will be lost upon an unsorted append.

Applying the parted attribute creates an index dictionary that maps each unique
output value to the position of its first occurrence

Parted (`p#)
`p# means the list is parted and identical items are stored contiguously.
The range is an int or temporal type having an underlying int value, such as
years, months, days, etc. You can also partition over a symbol provided it is
enumerated. 
Applying the parted attribute creates an index dictionary that maps each unique
output value to the position of its first occurrence.

Grouped (`g#)
`g# means the list is grouped. An internal dictionary is built and maintained which
maps each unique item to each of its indices, requiring considerable storage space.
For a list of length L containing u unique items of size s, this will be (L × 4) + (u
× s) bytes.

Unique (`#u)
Applying the unique attribute (`u#) to a list indicates that the items of the list are
distinct. Knowing that the elements of a list are unique dramatically speeds
up distinct and allows q to execute some comparisons early.
--Searches on `u# lists are done via a hash function.

RemovingAttributes
Attributes can be removed by applying `#.

@[ `.; `L ; `s#] / Functional apply, i.e. to the variable list L
/ in the default namespace (i.e. `.) apply
/ the sorted `s# attribute

Update `s#time from `tab

#dynamic queries
?[t;c;b;a] / for select
![t;c;b;a] / for update

/ select from t
?[t;();0b;()] 

q)wherecon: enlist (>;`p;40)
q)?[`t;wherecon;0b;()] / select from t where p>40

Functional Exec
The functional form of exec is a simplified form of select.
q)?[t;();();`n] / exec n from t (functional form of exec)
`ibm`msft`samsung`apple
q)?[t;();`n;`p] / exec p by n from t (functional exec)

Functional Update
The functional form of update is completely analogous to that of select. In the
following example, the use of enlist is to create singletons, to ensure that input
entities are lists.
q)c:enlist (>;`p;0)
q)b: (enlist `n)!enlist `n
q)a: (enlist `p) ! enlist (max;`p)
q)![t;c;b;a]

Functional delete
Functional delete is a simplified form of functional update. Its syntax is as follows:
![t;c;0b;a] / t is a table, c is a list of where constraints, a is a 	 list of column names

q)![t; enlist (=;`p; 40); 0b;`symbol$()] 

#unkey a table
0!tab


#serialize/deserialize
 `:/data/t set ([] s:`a`b`c; v:100 200 300)
`:/data/t

    get `:/data/t

apply: {[container; indices; function]
    result: container;
    result[indices]: function each container indices;
    : result;
    }
	

