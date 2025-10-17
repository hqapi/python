from hqapi.screenshot import ScreenshotClient

# Set your token, get yours at https://hqapi.com/
SCREENSHOT_API_TOKEN="--put--your--token--here--"

client = ScreenshotClient(token=SCREENSHOT_API_TOKEN)
image_data = client.create(url="https://hqapi.com/")

# Save to disk
with open("screenshot.png", "wb") as f:
    f.write(image_data)
    

