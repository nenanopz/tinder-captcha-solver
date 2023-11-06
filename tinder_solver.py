import capsolver
from urllib.parse import urlparse

# Change this information
capsolver.api_key = "Your pay per usage key"

def solve_funcaptcha_tinder():
    solution = capsolver.solve({
    "type": "FunCaptchaTaskProxyLess",
        "websiteURL": "https://tinder.com/",
        "websitePublicKey": "15485B1D-E5A1-0166-162C-FF8EBF968955",
        "funcaptchaApiJSSubdomain": "https://tinder-api.arkoselabs.com/"
    })
    return solution

def main():
    
    print("Solving tinder captcha")
    solution = solve_funcaptcha_tinder()
    
    token = solution["token"]
    
    print("Token Solution " + token)
    
if __name__ == "__main__":
    main()
