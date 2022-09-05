class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # for every course initially, we want to map it to an empty list
        hashMap = { i:[] for i in range(numCourses)}
        # map each course to its prereq
        for course, pre in prerequisites:
            hashMap[course].append(pre)
        # keep track of visited course nodes in a set
        visited = set()
        def dfs(course):
            # if the course has already been visited, then there is a loop within the graph and it is impossible to take all courses
            if course in visited:
                return False
            # if there are no prereqs for the course, then u can just take it lol
            if hashMap[course] == []:
                return True
            # proceed to add the course to the visited set if edge cases aren't satisified
            visited.add(course)
            # preforming dfs, visiting every prereq for the course that we are visiting
            for prereq in hashMap[course]:
                if dfs(prereq) == False:
                    return False
            # we are done with the course, so we can remove it from the visited set
            visited.remove(course)
            # we know now that from this course, every course can be taken. There is no need to redo work if this node is visited again, so just set no prereqs to the course so it is automatically going to return true in future dfs calls. 
            hashMap[course] = []
            return True
        # the graph can be unconnected. Therefore, we have to ensure that we visiting every node by preforming dfs on every course.
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True
