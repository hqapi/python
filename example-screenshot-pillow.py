from PIL import Image
import io
from hqapi.screenshot import ScreenshotClient

# Set your token, get yours at https://hqapi.com/
SCREENSHOT_API_TOKEN="--put--your--token--here--"

client = ScreenshotClient(token=SCREENSHOT_API_TOKEN)
image_data = client.create(url="https://hqapi.com/")

# Convert image blob to PIL Image
image = Image.open(io.BytesIO(image_data))

# Display it (for testing)
image.show()

# Save it to a file
image.save("screenshot.png")