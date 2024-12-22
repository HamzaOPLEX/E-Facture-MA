#!/bin/bash

# Prompt for commit message
read -p "Enter commit message: " commit_message

# Add all changes
git add .

# Commit changes
git commit -m "$commit_message"

# Push changes to the current branch
git push

echo "Changes have been pushed successfully!"
