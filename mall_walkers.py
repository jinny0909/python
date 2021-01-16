#!/usr/bin/env pyhon3
# -*- coding: utf-8 -*-
"""
@author: Kyoungjin Lim
"""

import random
import frac 

class Node: 
    
       """Class for creating an instance of a Node"""
    
       def __init__(self, id, connected_nodes): 
           
           """
           Parameters 
           -------
            
           id : TYPE, string
               DESCRIPTION. unique id of a node
           connected_nodes: TYPE, string array 
               DESCRIPTION. list of connecting_nodes id 
    
           Returns
           -------
           Creates an instance of node  
    
           """
           
           self.id = id 
           
           #connected nodes - outgoing nodes only 
           self.connected_nodes = connected_nodes 
           #self.movement_probs should be calculated based on connected_nodes
           #the list of prob of moving to each connected node 
           
           prob_list = []
           
           prob = frac.Frac(1, len(connected_nodes))
           
           for i in range(len(connected_nodes)): 
               prob_list.append(prob)
           
           self.movement_probs = prob_list

          
           return 
       

    
 
class Walker: 
    
    """Class for creating an instance of a Walker"""
    
    def __init__(self, current_node_id): 
        
        """
        Parameters 
        -------
        
        num : TYPE, string
            DESCRIPTION. id of a current_node
       
        Returns
        -------
        Creates an instance of a Walker

        """
        
        #may find it useful to create a setter method to indirectly set 
        #current_node_id so no need for direct mutation 
        
        self.current_node_id = current_node_id
        
        return
    
    def set_current_node_id(self, current_node_id): 
        
        """
        Parameters 
        -------
        
        num : TYPE, string
            DESCRIPTION. current_node id 

        Returns
        -------
        Sets current_node_id of a walker

        """
        
        self.current_node_ide = current_node_id
        
        return 
    


def run_simulation(filename, n): 
    """

    Parameters
    ----------
    def run_simulation :  
        filename (string): name of the input text file 
        n (int): number of walkers 

    Returns 
    -------
    a list of the node names based on the rank in descending order 
    """
    
    # read file, create new graph with the given connection info 
    my_file = open(filename, 'r')
    
    #keys: node id 
    #values: array of ougoing node ids 
    input_dic = {}
