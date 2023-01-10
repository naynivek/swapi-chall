git config --global user.email "runner@example.com"
git config --global user.name "Runner"
git checkout -b $1
mkdir -p components
#Download the packages
touch components/$2
git add .
git commit -m "new branch $1"
git push --set-upstream origin $1
git checkout develop
git merge $1
git push
