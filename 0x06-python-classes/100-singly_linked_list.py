#!/usr/bin/python3


class Node:
    """
    Node class for a singly linked list
    """
    def __init__(self, data, next_node=None):
        """
        initialization called when instance of class created
        """
        if self.__validate_data(data):
            self.__data = data
        if self.__validate_node(next_node):
            self.__next_node = next_node

    @property
    def data(self):
        """
        get the data attribute
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        set the data attribute
        """
        if self.__validate_data(value):
            self.__data = value

    @property
    def next_node(self):
        """
        get the node attribute
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        set the node attribute
        """
        if self.__validate_node(value):
            self.__next_node = value

    def __validate_data(self, data):
        """
        validates the data, checking its type
        Returns true or false if valid or not respectively
        """
        if isinstance(data, int):
            return True
        return False

    def __validate_node(self, node):
        """
        validates the node, checking it's a node object
        Returns true or false if valid or not respectively
        """
        if isinstance(node, Node) or node is None:
            return True
        return False


class SinglyLinkedList:
    """
    contains nodes for a singly linked list and methods for ->
    insertion
    """
    def __init__(self):
        """
        initialization called when instance of class created
        """
        self.__head = None

    def __str__(self):
        """
        used by print to print linked list
        """
        tmp = self.__head
        string = ""
        while tmp is not None:
            string += str(tmp.data)
            tmp = tmp.next_node
            if tmp is not None:
                string += '\n'
        return string

    def sorted_insert(self, value):
        """
        inserts a new Node into the correct sorted position
                                            (based on data)
        """
        tmp = self.__head
        if tmp is None:
            self.__head = Node(value)
            return

        prev = None
        while tmp is not None:
            if (tmp.next_node is None or tmp.next_node.data >= value):
                if (tmp.data >= value):
                    next_n = tmp
                    tmp = Node(value)
                    tmp.next_node = next_n
                    if prev is not None:
                        prev.next_node = tmp
                    else:
                        self.__head = tmp
                else:
                    next_n = tmp.next_node
                    tmp.next_node = Node(value)
                    tmp.next_node.next_node = next_n
                return

            prev = tmp
            tmp = tmp.next_node
