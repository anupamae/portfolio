
        function openGitHub(github_link) {
            if (github_link) {
                // Open the GitHub repository in a new tab or window
                window.open(github_link, '_blank');
            } else {
                // Handle the case where the GitHub URL is not available
                alert("GitHub repository URL not provided.");
            }
        }
  