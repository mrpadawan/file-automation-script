# How to trigger a release

```powershell
python src/update_version.py 1.3.0
git add VERSION README.md src/shared/version.py
git commit -m "Bump version to 1.3.0"
git push origin main

git tag -a v1.3.0 -m "Version 1.3.0"
git push origin v1.3.0
```
