import requests
import socket
from urllib.parse import urljoin, urlparse

#Commom directories
common_dirs = [
    # --- Administrative ---
    "admin", "manage", "portal", "controlpanel", "wp-admin",
    
    # --- Development & Versioning ---
    ".git", ".env", ".bash_history", "composer.json", "package.json",
    
    # --- Backups & Data ---
    "backup", "old", "archive", "sql", "db", "dump.sql", "backup.zip",
    
    # --- Config & Setup ---
    "config", "settings", "setup", "install", ".htaccess", "web.config",
    
    # --- Debugging & Info ---
    "phpinfo.php", "test", "demo", "logs", "error_log",
    
    # --- API & Documentation ---
    "api/v1", "swagger", "docs", "graphql", "v2"
]



# Modern Security Header Configuration
security_headers = {
    # --- Integrity & Injection Prevention ---
    "Content-Security-Policy": "default-src 'self'; script-src 'self'; object-src 'none';",
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    
    # --- Connection Security ---
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains; preload",
    
    # --- Privacy & Information Leakage ---
    "Referrer-Policy": "strict-origin-when-cross-origin",
    
    # --- Feature & Hardware Control ---
    "Permissions-Policy": "camera=(), microphone=(), geolocation=(), interest-cohort=()",
    
    # --- Cross-Origin Isolation (Spectre Protection) ---
    "Cross-Origin-Opener-Policy": "same-origin",
    "Cross-Origin-Embedder-Policy": "require-corp",
    "Cross-Origin-Resource-Policy": "same-origin"
}

#SQL injection
sqli_payload = "' or  '1' = '1''"

#Cross site scripting
XSS_payload = "<script>alert(1)</script>"

TimeOut = 5



#Utility Functions

#to check if the web is active or reachable

def is_web_reachable(url):
    try:
        response = requests.get(url,timeout=TimeOut)
        return response.status_code < 500
    except requests.RequestException:
        return False


#getting response from the web

def get_response(url):
    try:
        return requests.get(url,timeout=TimeOut)
    except requests.RequestException:
        return None


#checking security headers        

def web_headers_scan(response):
    missing = []

    for header in security_headers:
        if header not in response.headers:
            missing.append(header) 
    return missing



#scanning directories for access

def dir_scan(url):
    dir = []
    for directory in common_dirs:
        test_url = urljoin( url + '/', directory)
        try:
            r =requests.get(test_url,timeout=TimeOut)
            if r.status_code in [200,301,302]:
                dir.append(directory)

        except requests.RequestException:
            pass
    return dir


#checking xss 

def check_xss(url):
    test_url = f"{url}?q={XSS_payload}"
    try :
        r = requests.get(test_url,timeout=TimeOut)
        if XSS_payload in r.text:
            return True
    except requests.RequestException:
        pass
    return False


#checking sql injections prevention

def check_sql(url):
    test_url = f"{url}?id{sqli_payload}"
    try:
        r = requests.get(test_url,TimeOut)
        error_signatures = [
            "sql syntax",
            "mysql",
            "syntax error",
            "unclosed quotation"
        ]
        for error in error_signatures:
            if error.lower() in r.text.lower():
                return True
    except requests.RequestException:
        pass
    return False



    #   MAIN PROGRAM


def scan_web(target_url):
    print("Simple Web scanner Using python")
    print(f"target {target_url}")


    if not is_web_reachable(target_url):
        print("Web is not active or reachable")
        return

    print("Web is reachable")

    response = get_response(target_url)
    if not response:
        print("Failed")
        return


    missing_headers = web_headers_scan(response)
    if missing_headers:
        print("Missing Security Headers")
        for i in missing_headers:
            print("           " + i)
    else:
        print("Present All headers")

    dirs = dir_scan(target_url)
    if dirs:
        print("Found Directories")
        for i in dirs:
            print("           " + i)
    else:
        print("Not Dirs")

        
    if check_xss(target_url):
        print("POssible refleted XSS detect")
    else:
        print("no detection")

    if check_sql(target_url):
        print("Possible injection")
    else:
        print("Prevented injections")

    print("scan completed")






if __name__ == "__main__":
    target_url = input("ENter url ex- https://google.com \n")
    scan_web(target_url)

