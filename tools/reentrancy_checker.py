def scan_for_reentrancy(contract_code):
    vulnerabilities = []
    if "call{value:" in contract_code and "state = " in contract_code:
        vulnerabilities.append("Potential Reentrancy: State update after external call.")
    
    if not vulnerabilities:
        return "No common reentrancy patterns found."
    return vulnerabilities

if __name__ == "__main__":
    print("Starting Security Scan...")
    # Simulation
    print(scan_for_reentrancy("function withdraw() { msg.sender.call{value: amt}(''); state = DONE; }"))
