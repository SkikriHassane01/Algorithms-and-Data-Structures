class Node:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Node(homepage)
        

    def visit(self, url: str) -> None:
        new_node = Node(url)
        self.current.next = new_node
        new_node.prev = self.current
        self.current = new_node
        new_node.next = None 

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.current.prev != None:
                self.current = self.current.prev
        return self.current.val

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.current.next != None:
                self.current = self.current.next
        return self.current.val
    

if __name__ == "__main__":
    browserHistory = BrowserHistory("leetcode.com")
    browserHistory.visit("google.com")       # You are in "leetcode.com". Visit "google.com"
    browserHistory.visit("facebook.com")     # You are in "google.com". Visit "facebook.com"
    browserHistory.visit("youtube.com")      # You are in "facebook.com". Visit "youtube.com"
    print(browserHistory.back(1))            # You are in "youtube.com", move back to "facebook.com" return "facebook.com"
    print(browserHistory.back(1))            # You are in "facebook.com", move back to "google.com" return "google.com"
    print(browserHistory.forward(1))         # You are in "google.com", move forward

    browserHistory.visit("linkedin.com")     # You are in "google.com". Visit "linkedin.com"
    print(browserHistory.forward(2))         # You are in "linkedin.com", you cannot move forward any steps.
    print(browserHistory.back(2))            # You are in "linkedin.com", move back two steps to "google.com" return "google.com"
    print(browserHistory.back(7))            # You are in "google.com", you can
