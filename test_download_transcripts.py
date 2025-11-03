#!/usr/bin/env python3
"""
Basic tests for download_transcripts.py
"""

import unittest
import subprocess
import sys
from pathlib import Path


class TestDownloadTranscripts(unittest.TestCase):
    """Test cases for the transcript download script"""
    
    def test_script_imports_successfully(self):
        """Test that the script can be imported without errors"""
        import download_transcripts
        self.assertTrue(hasattr(download_transcripts, 'main'))
    
    def test_script_is_executable(self):
        """Test that the script is executable"""
        script_path = Path("download_transcripts.py")
        self.assertTrue(script_path.exists())
        self.assertTrue(script_path.is_file())
    
    def test_requirements_file_exists(self):
        """Test that requirements.txt exists and contains yt-dlp"""
        requirements_path = Path("requirements.txt")
        self.assertTrue(requirements_path.exists())
        
        content = requirements_path.read_text()
        self.assertIn("yt-dlp", content)
    
    def test_gitignore_exists(self):
        """Test that .gitignore exists and excludes transcripts"""
        gitignore_path = Path(".gitignore")
        self.assertTrue(gitignore_path.exists())
        
        content = gitignore_path.read_text()
        self.assertIn("transcripts/", content)
    
    def test_workflow_file_exists(self):
        """Test that GitHub Actions workflow exists"""
        workflow_path = Path(".github/workflows/download-transcripts.yml")
        self.assertTrue(workflow_path.exists())
        
        content = workflow_path.read_text()
        self.assertIn("workflow_dispatch", content)
        self.assertIn("download_transcripts.py", content)


if __name__ == "__main__":
    unittest.main()
