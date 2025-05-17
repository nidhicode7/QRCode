import qrcode

def generate_qr(data, filename="myqr.png"):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"✅ QR code generated and saved as {filename}")

def main():
    print("🌀 Welcome to Smart QR Generator!")
    print("Enter the type of data you want to convert into a QR code:")
    print("1. Website URL")
    print("2. Email Address")
    print("3. Phone Number")
    print("4. LinkedIn Profile")
    print("5. GitHub Profile")
    print("6. Custom Text")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        data = input("Enter the website URL: ")
    elif choice == "2":
        email = input("Enter the email address: ")
        data = f"mailto:{email}"
    elif choice == "3":
        phone = input("Enter the phone number: ")
        data = f"tel:{phone}"
    elif choice == "4":
        data = input("Enter the LinkedIn profile URL: ")
    elif choice == "5":
        data = input("Enter the GitHub profile URL: ")
    elif choice == "6":
        data = input("Enter your custom text: ")
    else:
        print("❌ Invalid choice. Exiting.")
        return

    filename = input("Enter filename to save QR (like `myqr.png`): ")
    generate_qr(data, filename)

if __name__ == "__main__":
    main()
