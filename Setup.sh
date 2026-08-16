#!/bin/bash

echo "Installing dependencies..."

# Function to detect the package manager
detect_package_manager() {
    if command -v apt-get &> /dev/null; then
        echo "apt"
    elif command -v dnf &> /dev/null; then
        echo "dnf"
    elif command -v pacman &> /dev/null; then
        echo "pacman"
    else
        echo "unknown"
    fi
}

# Install dependencies based on the package manager
PACKAGE_MANAGER=$(detect_package_manager)

case $PACKAGE_MANAGER in
    apt)
        echo "Detected Ubuntu/Debian-based system"
        echo "Installing build essentials..."
        sudo apt-get update
        sudo apt-get install -y ffmpeg
        ;;
    dnf)
        echo "Detected Fedora/RHEL-based system"
        echo "Installing build essentials..."
        sudo dnf install -y ffmpeg
        ;;
    pacman)
        echo "Detected Arch-based system"
        echo "Installing build essentials..."
        sudo pacman -S --needed ffmpeg
        ;;
    *)
        echo "Unsupported package manager. Please install the following packages manually:"
        echo "- fmmpeg"
        exit 1
        ;;
esac

    if [[ ! -d "$VIRTUAL_ENV" ]]; then
        python3 -m venv env
    fi

    source $VIRTUAL_ENV/bin/activate
    pip install -r requirements.txt

    echo "All done! If your package manager wasn't recognized, this won't work. If it did, then you can run by doing: python3 __main__.py <option>"

exit 0
