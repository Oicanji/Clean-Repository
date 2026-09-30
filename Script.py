import argparse
import subprocess
import sys


def run(command):
    result = subprocess.run(command, text=True)

    if result.returncode != 0:
        sys.exit(result.returncode)


def main():
    parser = argparse.ArgumentParser(
        description="Reescreve autor e committer de todos os commits."
    )

    parser.add_argument("username", help="Nome/username que será usado nos commits")
    parser.add_argument("email", help="E-mail que será usado nos commits")

    args = parser.parse_args()

    print("Reescrevendo histórico...")
    print("Username:", args.username)
    print("Email:", args.email)

    run([
        "git",
        "filter-repo",
        "--force",
        "--commit-callback",
        f"""
commit.author_name = b'{args.username}'
commit.author_email = b'{args.email}'
commit.committer_name = b'{args.username}'
commit.committer_email = b'{args.email}'
"""
    ])

    print("\nHistórico reescrito com sucesso.")


if __name__ == "__main__":
    main()
