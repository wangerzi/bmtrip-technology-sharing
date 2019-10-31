| options | options             | description                                              |
| ------- | ------------------- | -------------------------------------------------------- |
| -n      | --dry-run           | show what will happen and would not apply it eventually. |
| -f      | --force             | add ignored file.                                        |
| -A      | --no-ignore-removal | update index with file in work tree.(about removal file) |
| -N      | --intent-to-add     | mark a new file tracked.                                 |



### Conception

> mark file and content to staged status for next commit.

---

### Demo

1. init a git repository

```bash
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        a
        b
        c

nothing added to commit but untracked files present (use "git add" to track)
```

2. try `git add --dry-run`

> options: dry run [ -n, --dry-run ]

```bash
$ git add -n .
add 'a'
add 'b'
add 'c'

$ git add -An
add 'a'
add 'b'
add 'c'

$ git add -un

```

3. try `git add --intent-to-add`

> options: intent to add

```bash
# git add without option
$ git add a
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   a

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        b
        c
        
# git add with option `--intent-to-add`
$ git add --intent-to-add b
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   a

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        new file:   b

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        c
```

4. try `git add -e --<pathspec>`

> options: edit

```bash
$ echo cc >> c
# set track for "c"
$ git add -N c
$ git diff
diff --git a/c b/c
new file mode 100644
index 0000000..2f773ae
--- /dev/null
+++ b/c
@@ -0,0 +1,2 @@
+c
+cc

# edit add info, only add oneline
$ git add -e c
hint: Waiting for your editor to close the file...
 [main 2019-10-31T05:21:53.995Z] update#setState idle
 
# inspect status
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   a
        new file:   b
        new file:   c

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   c
        
# inspect diff index..not staged
$ git diff c
diff --git a/c b/c
index f2ad6c7..2f773ae 100644
--- a/c
+++ b/c
@@ -1 +1,2 @@
 c
+cc

# inspect diff last commit..staged
$ git diff --staged c
diff --git a/c b/c
new file mode 100644
index 0000000..f2ad6c7
--- /dev/null
+++ b/c
@@ -0,0 +1 @@
+c

```

