### Practice Quiz: Branching & Merging
* **Total points: 5**
* **Score: 100%**

### 1. When we merge two branches, one of two algorithms is used. If the branches have diverged, which algorithm is used?

☑️ **three-way merge**

⬜ fast-forward merge

⬜ merge conflict

⬜ orphan-creating merge

✅Correcto

Excellent! A three-way-mergeoccurs when the two commits have diverged previously, and a new commit is created.

### 2. The following code snippet represents the result of a merge conflict. Edit the code to fix the conflict and keep the version represented by the current branch.

``` PYTHON
print("Keep me!")
```



### 3. What command would we use to throw away a merge, and start over?

⬜ git checkout -b <branch>

☑️ **git merge --abort**

⬜ git log --graph --oneline

⬜ git branch -D <name>

✅ Correcto

Right on! If there are merge conflicts, the --abort flag can be used to abort the merge action.

### 4. How do we display a summarized view of the commit history for a repo, showing one line per commit?

⬜ git log --format=short

⬜ git branch -D <name>

☑️ **git log --graph --oneline**

⬜ git checkout -b <branch>

✅Correcto

Awesome! The commandgit log --graph --oneline shows a summarized view of the commit history for a repo.

### 5. The following script contains the result of a merge conflict. Edit the code to fix the conflict, so that both versions are included.

``` PYTHON

def main():
    print("Start of program>>>>>>>")
    print("End of program!")

main()
```
✅Correcto

Great work! Now the code has both versions without any
conflicts!
