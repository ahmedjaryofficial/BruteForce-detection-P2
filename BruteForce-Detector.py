with open("sample_auth.log", "r") as file:
    for line in file:

        if "Failed password" in line:
            words = line.split()
            from_index = words.index("from")
            ip_address = words[from_index + 1]
            failed_attempts = {}
            if ip_address in failed_attempts:
                failed_attempts[ip_address] += 1
            else:
                failed_attempts[ip_address] = 1
                for ip, count in failed_attempts.items():
                    print(f"{ip}: {count} total failed attempts")
