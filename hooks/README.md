To enable the git hooks in your git repo, run the following from the repo root:

```bash
rm -rf .git/hooks && ln -s -f ../hooks .git/
```
