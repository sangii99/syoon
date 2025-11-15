import heapq
from functools import total_ordering
from graph_library import *

@total_ordering
class SpecialSorted:

    def __init__(self, element, value):
        self.element = element
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        return self.value < other.value

class PriorityQueue:

    def __init__(self, sortkey = lambda x : x):
        self.content = []
        self.sortkey = sortkey

    def add(self, item):
        heapq.heappush(self.content, SpecialSorted(item, self.sortkey(item)))

    def peek(self):
        return self.content[0].element if self.content else None

    def poll(self):
        return heapq.heappop(self.content).element if len(self.content) > 0 else None

    def is_empty(self):
        return len(self.content) == 0

    def __str__(self):
        return str([item.element for item in self.content])


def shortest_path(graph, src, dest):
    INF = float('inf')

    dist = {node: INF for node in graph.nodes}
    dist[src] = 0
    parent = {src: None} # {Node('22'): None, Node('1'): Node('22')} means node 22 is source, no parebt, and node 1 comes from node 22
    visited = set()

    pq = PriorityQueue(sortkey=lambda node: dist[node]) # sorting priority queue by distance
    pq.add(src)

    while not pq.is_empty():
        print("pq before poll: ", pq)
        u = pq.poll()
        print("pq after poll: ", pq)
        print("u: ", u)
        if u in visited:
            continue
        visited.add(u)
        print("visited: ", visited)

        if u == dest:
            break
        print("neighbouring vertices: ", graph.get_outgoing_edges(u))
        for e in graph.get_outgoing_edges(u):
            print("e: ", e)
            v = e.get_destination()
            print("v: ", v)
            w = e.weight if e.weight is not None else 1
            print("w: ", w)
            if v in visited:
                continue
            new = dist[u] + w # new distance is distance from the previous nodes + current node's distance
            print("new: ", new)
            if new < dist[v]:
                print("now we are updating the neighboring distances to the new one")
                dist[v] = new #updating v's distance to new
                print("dist: ", dist)
                parent[v] = u # v coming from node u
                print("parent: ", parent)
                pq.add(v)
            print("pq after adding v: ", pq)

    # If unreachable, return None (not an empty list)
    if dist[dest] == INF:
        return None

    # Reconstruct path
    path = []
    cur = dest
    while cur is not None:
        print("cur: ", cur)
        path.append(cur)
        cur = parent.get(cur)
        print("path: ", path)

    path.reverse()
    print("path: ", path)
    return path


def main():
    graph01 = directed_graph_from_dict({'22': ['1'], '1': ['9', '14', '20', '37'], '9': ['42', '37', '18'], '42': ['23', '31', '22'], '23': ['40', '44'], '40': ['18', '13', '39'], '18': ['25', '36'], '25': ['26', '21', '4', '17'], '26': ['32', '43', '22'], '32': ['43', '35', '21', '4'], '43': ['13'], '13': ['37', '43', '27'], '37': ['3', '14', '30', '18'], '3': ['8', '39', '33', '30'], '8': ['2', '13', '9'], '2': ['24', '15', '34', '19'], '24': ['38', '23', '12'], '38': ['31', '34'], '31': ['16', '17', '37', '8', '23', '40'], '16': ['14', '18'], '14': ['4'], '4': ['41', '25', '8'], '41': ['6', '38', '37'], '6': ['35', '41'], '35': ['15', '34', '21', '3'], '15': ['33', '7', '37', '31', '26'], '33': ['11', '28', '5'], '11': ['19', '5'], '19': ['27', '42'], '27': ['12', '1', '43', '2', '42'], '12': ['10', '19'], '10': ['5', '36', '28', '27', '26'], '5': ['29', '17', '3'], '29': ['21', '13'], '21': ['17', '36', '4', '7', '40'], '17': ['36', '21', '29', '22', '13', '32', '28', '35', '14'], '36': ['30', '43'], '30': ['28', '12'], '28': ['34', '1', '17'], '34': ['39', '35', '3', '27'], '39': ['20', '5', '42', '40', '15'], '20': ['7', '37', '4', '25', '30', '12'], '7': ['44', '25'], '44': ['34', '28', '23']}, weights = {('22', '1'): 84, ('1', '9'): 43, ('9', '42'): 12, ('42', '23'): 76, ('23', '40'): 7, ('40', '18'): 24, ('18', '25'): 11, ('25', '26'): 87, ('26', '32'): 24, ('32', '43'): 37, ('43', '13'): 57, ('13', '37'): 64, ('37', '3'): 53, ('3', '8'): 86, ('8', '2'): 58, ('2', '24'): 37, ('24', '38'): 51, ('38', '31'): 70, ('31', '16'): 33, ('16', '14'): 32, ('14', '4'): 45, ('4', '41'): 17, ('41', '6'): 69, ('6', '35'): 94, ('35', '15'): 75, ('15', '33'): 30, ('33', '11'): 35, ('11', '19'): 98, ('19', '27'): 11, ('27', '12'): 78, ('12', '10'): 80, ('10', '5'): 69, ('5', '29'): 86, ('29', '21'): 74, ('21', '17'): 57, ('17', '36'): 10, ('36', '30'): 36, ('30', '28'): 57, ('28', '34'): 26, ('34', '39'): 10, ('39', '20'): 59, ('20', '7'): 65, ('7', '44'): 18, ('15', '7'): 17, ('31', '17'): 70, ('13', '43'): 31, ('38', '34'): 64, ('37', '14'): 42, ('3', '39'): 20, ('29', '13'): 45, ('33', '28'): 49, ('9', '37'): 12, ('31', '37'): 13, ('35', '34'): 18, ('20', '37'): 10, ('26', '43'): 92, ('3', '33'): 21, ('19', '42'): 56, ('27', '1'): 12, ('10', '36'): 97, ('17', '21'): 66, ('15', '37'): 42, ('21', '36'): 9, ('23', '44'): 55, ('24', '23'): 41, ('42', '31'): 62, ('25', '21'): 10, ('34', '35'): 11, ('39', '5'): 52, ('34', '3'): 26, ('21', '4'): 84, ('10', '28'): 39, ('32', '35'): 42, ('44', '34'): 30, ('31', '8'): 40, ('28', '1'): 68, ('20', '4'): 11, ('34', '27'): 81, ('5', '17'): 33, ('7', '25'): 68, ('15', '31'): 74, ('44', '28'): 39, ('32', '21'): 82, ('35', '21'): 70, ('11', '5'): 2, ('17', '29'): 14, ('37', '30'): 6, ('24', '12'): 91, ('27', '43'): 93, ('20', '25'): 93, ('8', '13'): 41, ('41', '38'): 14, ('5', '3'): 51, ('40', '13'): 36, ('25', '4'): 56, ('16', '18'): 60, ('20', '30'): 58, ('41', '37'): 6, ('10', '27'): 13, ('1', '14'): 71, ('39', '42'): 86, ('3', '30'): 24, ('12', '19'): 77, ('8', '9'): 25, ('30', '12'): 65, ('33', '5'): 10, ('27', '2'): 66, ('4', '25'): 3, ('37', '18'): 99, ('32', '4'): 15, ('1', '20'): 1, ('35', '3'): 23, ('6', '41'): 1, ('2', '15'): 98, ('36', '43'): 43, ('17', '22'): 91, ('2', '34'): 10, ('21', '7'): 91, ('25', '17'): 74, ('28', '17'): 99, ('4', '8'): 98, ('17', '13'): 52, ('1', '37'): 55, ('17', '32'): 43, ('26', '22'): 25, ('20', '12'): 76, ('31', '23'): 79, ('17', '28'): 33, ('15', '26'): 46, ('40', '39'): 34, ('21', '40'): 27, ('17', '35'): 22, ('39', '40'): 64, ('27', '42'): 75, ('9', '18'): 55, ('31', '40'): 70, ('13', '27'): 91, ('17', '14'): 74, ('39', '15'): 3, ('10', '26'): 87, ('44', '23'): 82, ('42', '22'): 17, ('18', '36'): 86, ('2', '19'): 81})
    src = graph01.get_node_from_name('22')
    dest = graph01.get_node_from_name('44')
    shortest_path(graph01, src, dest)

main()