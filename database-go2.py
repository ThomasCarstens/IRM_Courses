#Database structure: fixed Table called "Phonebook"
#LOOKUP()
#ADDNEW()

#Support multiple tables, with any number of rows, with any data type
        #IMPLEMENTATION: Using linked lists.

#Index on specific rows.
        #IMPLEMENTATION: A dict for column names | One for specific rows

#Build/rebuild index.
        #IMPLEMENTATION: From table ->
#Use a query language.
#SELECT()
##############################################################

""" STEP 1: SET UP DATA STRUCTURES """

"""
  Binary tree with left and right node & value
  The Node class also reprents the entire Tree, by using it as the Root node
"""
class BNode:
    def __init__(self, val):
        self.left_node : BNode = None
        self.right_node :BNode = None
        self.value = val

    """
        Check if prints.
    """
    def PrintTree(self):
        if self.left_node:
            self.left_node.PrintTree()
        print(self.value),
        if self.right_node:
            self.right_node.PrintTree()
    """
        Returns an array of all the children nodes and the current node
        Greatest to lowest in this case.
    """
    def _get_nodes(self, nodes=[]):
        if self.right_node != None:
            self.right_node._get_nodes(nodes)
        nodes.append(self.value)
        print(self.value)
        if self.left_node != None:
            self.left_node._get_nodes(nodes)
        #print(self.value)

        return nodes

    """
        Insert value into the tree in balanced way.
    """
    def insert(self, data):
        #compare new node with parent
        if self.value:
            if data < self.value:
                if self.left_node is None:
                    self.left_node = BNode(data)
                else:
                    self.left_node.insert(data)
            elif data > self.value:
                if self.right_node is None:
                    self.right_node = BNode(data)
                else:
                    self.right_node.insert(data)
        else:
            self.value = data

    """
        Get array of values inferior to where condition
        NEED HELP.
    """
    def findinferior(self, where, nodes=[]):
        if where >= self.value:
            if self.left_node is None:
                return str(where)+" inferior to all database. No values."
            self._get_nodes(nodes)
        else:
            self.left_node.findinferior(where)
            print(str(self.value)+' is superior')
        return nodes[1:]

################# TESTING ################
# # ASSUMING: first value safely too high.
# nb_tree = BNode(100000000000000000)
# # ASSUMING: GETTING AN UNSORTED ARRAY.
# # Would the numbers come in as unsorted?
# # Most times just one number unsorted.
# # Maybe full sort needed once at the beginning.
# unbuilt_nb_array = [3,4,6,2,453,64,34,62,43]
# for nb in unbuilt_nb_array:
#     #print(nb)#v
#     nb_tree.insert(nb)
# built_nb_array = nb_tree._get_nodes()
# print(built_nb_array) #v
# nb_tree.PrintTree() #v
# print("findinferior: testing.")
# inf_array= nb_tree.findinferior(453)
# print(inf_array) #v
# # EXTENDABLE: currently nbs. Maybe with names too! (later)

# NEXT STEP: FIND in PHONEBOOK for WHERE < 200.

""" STEP 2: SET UP PHONEBOOK """

class Table:
    def __init__(self):
        self.my_dict={'Dave' : '001' , 'Ava': '002' , 'Joe': '003'}
        print("initialisation:")
        print("Name | Number")
        for x,y in self.my_dict.items():
            print(x, " | " , y)

    def viewtable(self):
        print("viewtable:\n")
        print("Name | Number")
        for x,y in self.my_dict.items():
            print(x, " | " , y)
        # FORMAT : using number of characters
        pass

    def addnew(self, key, value):
        # can store key-value pair
        self.my_dict[key] = value
        print(self.my_dict)
        # INTERFACE to be called upon some other way than addnew('Tom', '050')
        pass
        # CHECK: if nb is 10 digits long.
        pass

    def lookup(self, key):
        # can access by key
        print(self.my_dict[key])
        # to be stored
        pass

# #Table testing: unfixed phonebook.
phonebook1= Table() #v
# phonebook1.addnew('Tom', '050') #v
phonebook1.viewtable() #v

class Phonebook(Table):
    def __init__(self):
        self.my_array=[]
        self.my_dict={'Dave' : 345 , 'Ava': 62 , 'Joe': 742}
        print(self.my_dict.keys())

    def get_array_from_dict(self):
        # append each key into subarrays to create a table.
        for each_key in self.my_dict.keys():
            self.my_array.append([each_key,self.my_dict[each_key]])
        print("f: get array from dict:", self.my_array)
        return self.my_array

    def get_dict_from_array(self):
        # make subarrays into key-value pairs.
        new_dict = {}
        for i in range(self.my_array.__len__()):
            new_dict[i] = self.my_array[i][0]
        print("f: get dict from array: ", new_dict)

        # We should have an array with modulable elements i.e rows.
        for i in range(self.my_array.__len__()):
            self.my_array[i].append('insert element here')
            print (self.my_array[i])

        # Rather use linked lists, 2 items per node! see class below.
        pass

        # CHECK: one datatype per column.
        pass

        #self.id
        #self.nb
        #self.name
        pass

    def get_row_from_index(self, key):
        # INDEXING: dictionary key returns array row.
        print('get from index()')
#f        print(self.my_array[self.my_dict.get(key)])
        #passable for rows
        pass

    def get_element_from_index_and_single_select(self, key, select): ##?? Do I need a query language? does it refer to syntax within 'select'?
        # SELECT: which column of interest.
        # EXAMPLE INPUT: f('Dave', 'Number')
        my_array=self.get_array_from_dict()
        print(my_dict)
        print(my_array)
        col_dict={'Name':0, 'Number':1}
        print('get from index and SINGULAR select()')
        print(my_array[self.my_dict.get(key)][col_dict.get(select)])
        # ERROR...
        # INTERFACE: key, select within query language - SELECT: column names; KEY - must be rebuilt into a tree.
        pass

    def get_element_from_index_and_multiple_select(self, key, select): ##?? Do I need a query language? does it refer to syntax within 'select'?
        # SELECT: as a string to break up with commas.
        # EXAMPLE INPUT: f('Dave', 'Number,Name')
        clauses=select.split(',')
        print ("clauses: ", clauses)

        col_dict={'Name':0, 'Number':1}
        print('get from index and MULTIPLE select()')
        for clause in clauses:
            print(self.my_array[self.my_dict.get(key)][col_dict.get(clause)])
            #Great! We have output Number then Name, for Dave.
            #STEP IT UP: MAKING A TREE OF NUMBERS FOR THE WHERE.

        # INTERFACE: key, select within query language - SELECT: column names; KEY - must be rebuilt into a tree.
        pass

    def get_element_from_WHERE_and_single_SELECT(self, select, where): ##?? Do I need a query language? does it refer to syntax within 'select'?
        # EXAMPLE: f('Number', 43)
        #in 3 steps: table => phone_array => column tree => where.

        my_phone_array=[]
        phone_tree=BNode(100000000000000000)

        #table => phone_array
        column_names={'Name':0, 'Number':1, 'House_nb':2}
        print('get from WHERE and SINGULAR select(): ')
        print('my array: ', self.my_array)


        for i in range(len(self.my_array)):
           my_phone_array.append(self.my_array[i][column_names.get(select)])
           print ('phone_array: ', my_phone_array)

        #phone_array => column tree
        for nb in my_phone_array:
            #print(nb)#v
            phone_tree.insert(nb)
        my_built_nb_array = phone_tree._get_nodes()
        print("my built array: ", my_built_nb_array)

        #column tree => where
            #OPTION1: WHERE < 450
        print(phone_tree.findinferior(450))
            #OPTION2: WHERE = 450
        pass

        # INTERFACE: key, select within query language - SELECT: column names; KEY - must be rebuilt into a tree.
        pass


#Table testing: fixed phonebook.
phonebook1= Phonebook() #v
phonebook1.get_row_from_index('Dave') #v
#phonebook1.get_element_from_index_and_select('Dave', 2) #v
#phonebook1.addnew('Tom', '050') #we need to rebuild!!         ##?? Should I rebuild the dictionary - what's the use of a tree here?
#phonebook1.viewtable() #v

phonebook1.get_array_from_dict() #v
#NEEDED FOR BASE ARRAY!!

#phonebook1.get_dict_from_array() #v
print('INPUTS: Dave, Number')
#ERROR...
#phonebook1.get_element_from_index_and_single_select('Dave', 'Number')
print('INPUTS: Dave, Number, Name')
#ERROR...
#phonebook1.get_element_from_index_and_multiple_select('Dave', 'Number,Name')

phonebook1.get_element_from_WHERE_and_single_SELECT('Number', 43)
#ADD: command line for queries
pass
