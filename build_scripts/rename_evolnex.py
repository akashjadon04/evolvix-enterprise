import os

d = 'c:/projects/evolnex'

def replace_in_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Protect the email address
    email_placeholder = "evolvixtechnology@gmail.com"
    content = content.replace("evolvixtechnology@gmail.com", email_placeholder)

    # Protect github links if needed? Actually they said "across whole website, nothing should remain". 
    # But renaming github link might break it. Wait, the github link is akashjadon04/evolnex-enterprise.git
    # They said "wherever evolnex is written make it evolnex... just leave the email and attachments of email. and dont break anything."
    # A broken github repo link breaks something! Let's protect the github url.
    github_placeholder = "github.com/akashjadon04/evolvix-enterprise"
    content = content.replace("github.com/akashjadon04/evolvix-enterprise", github_placeholder)

    # Replace Evolnex variations
    content = content.replace("Evolnex", "Evolnex")
    content = content.replace("evolnex", "evolnex")
    content = content.replace("EVOLNEX", "EVOLNEX")

    # Restore placeholders
    content = content.replace(email_placeholder, "evolvixtechnology@gmail.com")
    content = content.replace(github_placeholder, "github.com/akashjadon04/evolvix-enterprise")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# Process all files recursively
for root, dirs, files in os.walk(d):
    if '.git' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith(('.html', '.js', '.css', '.md', '.json', '.py', '.txt')):
            replace_in_file(os.path.join(root, file))

# Rename files in assets
assets_dir = os.path.join(d, 'assets')
if os.path.exists(assets_dir):
    for f in os.listdir(assets_dir):
        if 'evolnex' in f:
            old_path = os.path.join(assets_dir, f)
            new_path = os.path.join(assets_dir, f.replace('evolnex', 'evolnex'))
            os.rename(old_path, new_path)

print("Renamed evolnex to evolnex successfully.")
