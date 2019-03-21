{
	"targets": [
		{
			"target_name": "winctl",
			"sources": [
				"src/WinCtlWrap.cc",
				"src/WinCtlWindow.cc"
			],
			"include_dirs": [
				"<!(node -e \"require('nan')\")"
			],
            "link_settings": {
                "libraries": ["C:\\Program Files (x86)\\Windows Kits\\10\\Lib\\10.0.17763.0\\um\\x64\\Psapi"]
            }
		}
	]
}
