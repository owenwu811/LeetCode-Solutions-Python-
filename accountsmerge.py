
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

721. Accounts Merge
Solved
Medium

Topics
Companies

Hint
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

 

Example 1:

Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Example 2:

Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
 



#python3 solution:


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails_dict = {}
        for index in range(len(accounts)): #we want to iterate through each sublist in the accounts list of lists
            for email in accounts[index][1:]: #start from index 1 in each sublist to the end because index 0 of each sublist is the name itself
                if email not in emails_dict: #if the index 1 through end string in each sublist in our dictionary as a key?
                    emails_dict[email] = set([index]) #if the index 1 string in our sublist is not a string key in our dictionary, then add it as a key and the value as a set with the index, which is the sublist we are on 
                else:
                    emails_dict[email].add(index) #if the index 1 string is in our dictionary as a key, just add the current sublist index in terms of the input into the corresponding set as the value to the key
        visited = [False] * len(accounts) #visited is a list with each sublist value as false - [False, False, False, False] because there are 4 sublists in the input list of lists accounts
        def dfs(acc_idx: int): #dfs(0) is called first
            emails = set() #in the 2nd dfs(2) call, emails becomes an empty set again
            visited[acc_idx] = True #[False, False, False, False] becomes [True, False, False, False]. in the 2nd dfs(2) call, [True, False, False, False] becomes [True, False, True, False]
            for email in accounts[acc_idx][1:]: #for email in accounts[0][1:], so iterating through 1st sublist index 1 to end (going through every single email in 1st sublist), 2nd time, accounts[2][1:], so iterating through 2nd sublist index, so email = "johnsmith@mail.com" again
                emails.add(email) #emailset becomes ("johnsmith@mail.com"). we now have another exact emailset "emails" that becomes  {"johnsmith@mail.com"}
                #emails_dict = {'johnsmith@mail.com': {0, 2}, 'john00@mail.com': {0}, 'johnnybravo@mail.com': {1}, 'john_newyork@mail.com': {2}, 'mary@mail.com': {3}}
                for master_id in emails_dict[email]: #master_id = 0, 2 because email = "johnsmith@mail.com" now
                    if visited[master_id]: #visited[0] happens to be True now - [True, False, False, False], so continue, but then next iteration visited[2] is False, so go to line after continue
                        continue
                    #emails = {'johnsmith@mail.com'} - emails is different from email
                    emails = emails | dfs(master_id) #we call dfs(2) since we didn't visited[2] = False
            return emails
        ans = []
        for index in range(len(accounts)): #just like line 2, we iterate through each sublist in the accounts list of lists
            if not visited[index]: #visited is a list, so visited[0] will always be False, so execute the inner block
                #question asks rest of elements are emails in SORTED ORDER HENCE SORTED(LIST(DFS(INDEX)))
                ans.append([accounts[index][0]] + sorted(list(dfs(index)))) #accounts is the input list of lists, so accounts[0][0] refers to "John" of the 1st sublist in the input
        return ans

#each account means each sublist in the input - Each entry in the accounts list is an "account," and it includes: The account holder's name (e.g., "John") and A list of email addresses associated with that account.

Detailed Example with DFS
Let's walk through the DFS for the first account (index 0):

python
Copy code
["John", "johnsmith@mail.com", "john00@mail.com"]
Initialization:

Start DFS from index 0.
Initialize an empty set: emails = set().
Mark account 0 as visited: visited[0] = True.
Collect Emails:

Iterate over emails in the current account: ["johnsmith@mail.com", "john00@mail.com"].
Add each email to the set:
Add "johnsmith@mail.com": emails = {"johnsmith@mail.com"}.
Add "john00@mail.com": emails = {"johnsmith@mail.com", "john00@mail.com"}.
Explore Connected Accounts:

For "johnsmith@mail.com", find connected accounts: {0, 2}.
Account 0 is already visited, so skip it.
Account 2 is not visited, so perform DFS on account 2.
Recursive DFS on Account 2:

Initialize an empty set: emails = set().
Mark account 2 as visited: visited[2] = True.
Collect emails from account 2: ["johnsmith@mail.com", "john_newyork@mail.com"].
Add "johnsmith@mail.com": emails = {"johnsmith@mail.com"}.
Add "john_newyork@mail.com": emails = {"johnsmith@mail.com", "john_newyork@mail.com"}.
For "johnsmith@mail.com", find connected accounts: {0, 2}.
Both are already visited, so no further DFS calls.
For "john_newyork@mail.com", connected accounts are only account 2, which is visited.
Union of Emails:

Union the collected emails from account 2: emails = {"johnsmith@mail.com", "john00@mail.com"} | {"johnsmith@mail.com", "john_newyork@mail.com"}.
Result: emails = {"johnsmith@mail.com", "john00@mail.com", "john_newyork@mail.com"}.
Return Result:

DFS for account 0 returns the set of unique emails connected to it: {"johnsmith@mail.com", "john00@mail.com", "john_newyork@mail.com"}.
Summary
"Account": Refers to each sublist in the accounts list.
DFS: Collects all unique emails associated with the initial account and all other accounts that share emails with it.
Result: Ensures that all connected accounts (via shared emails) are merged, regardless of the name, but retaining the name from the initial account.
This approach guarantees that accounts are merged based on shared emails, not just the account holder's name, thus fulfilling the requirement that accounts with the same name but no shared emails are not incorrectly merged.




Purpose of the Visited List
The visited list tracks which accounts (sub-lists in the accounts list) have been processed during the DFS traversal. It ensures that each account is visited exactly once, preventing redundant work and infinite loops.

Key Points:
Tracks Accounts: Keeps track of whether each account (sublist) has been visited.
Prevents Infinite Loops: Avoids revisiting accounts, which is crucial for preventing cycles in the graph of accounts and emails.
Ensures Efficiency: By marking accounts as visited, the algorithm avoids redundant processing of the same account, making the traversal more efficient.
Purpose of the Emails Set
The emails set collects all unique emails connected to the current account during the DFS traversal. It ensures that each email is included only once in the final merged account, handling the merging of accounts based on shared emails.

Key Points:
Collects Emails: Gathers all unique emails connected to the current account (sublist) and any accounts reachable through shared emails.
Ensures Uniqueness: Using a set ensures that each email appears only once, avoiding duplicates in the merged result.
Represents Connected Component: The set effectively represents the connected component in the graph formed by accounts and their shared emails.

#emails refer to strings within each sublist in the accounts list of lists

 #6/19/24 review:

 class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailsdict = {}
        for i in range(len(accounts)):
            for email in accounts[i][1:]:
                if email not in emailsdict:
                    emailsdict[email] = set([i])
                else:
                    emailsdict[email].add(i)
        visited = [False] * len(accounts) #have we visited this sublist or not
        def dfs(i):
            emails = set()
            visited[i] = True
            for em in accounts[i][1:]:
                emails.add(em)
                for n in emailsdict[em]:
                    if visited[n]:
                        continue
                    else:
                        emails = emails | dfs(n)
            return emails
        res = []
        for i in range(len(accounts)):
            if not visited[i]:
                res.append([accounts[i][0]] + sorted(list(dfs(i))))
        return res


