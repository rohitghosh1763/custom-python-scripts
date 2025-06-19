import asyncio
from pyppeteer import launch

async def main():
    # --- IMPORTANT ---
    # Paste the path to your Brave browser executable here.
    # The path below is the most common location for Brave on Windows.
    # Use double backslashes (\\) in the path.
    brave_executable_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

    html_content = """
    <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Shopify Developer Roadmap</title>
  <style>
    body {
      font-family: "Segoe UI", sans-serif;
      background: #f9f9f9;
      padding: 40px;
      color: #333;
    }
    h1 {
      text-align: center;
      margin-bottom: 40px;
      color: #2b6cb0;
    }
    ul.tree {
      list-style-type: none;
      padding-left: 20px;
    }
    ul.tree li {
      position: relative;
      padding-left: 20px;
      margin-bottom: 10px;
    }
    ul.tree li::before {
      content: '';
      position: absolute;
      top: 8px;
      left: 0;
      width: 12px;
      height: 12px;
      background-color: #2b6cb0;
      border-radius: 50%;
    }
    ul.tree li span {
      font-weight: bold;
      color: #1a202c;
    }
    .sub {
      margin-top: 5px;
      font-weight: normal;
      color: #4a5568;
    }
  </style>
</head>
<body>

  <h1>🌿 Shopify Developer Roadmap</h1>

  <ul class="tree">
    <li><span>Stage 1: Basics & Store Setup</span>
      <ul class="tree">
        <li>Create Shopify Partner Account</li>
        <li>Set up a Development Store</li>
        <li>Explore Admin Dashboard</li>
      </ul>
    </li>

    <li><span>Stage 2: Liquid & Theme Development</span>
      <ul class="tree">
        <li>Learn Liquid (loops, filters, conditions)</li>
        <li>Understand theme structure (layout, sections, templates)</li>
        <li>Use Shopify CLI for local development</li>
        <li>Style with Tailwind CSS / SCSS</li>
      </ul>
    </li>

    <li><span>Stage 3: Storefront Customization</span>
      <ul class="tree">
        <li>Work with Metafields</li>
        <li>Use Metaobjects</li>
        <li>Customize product, collection, and cart pages</li>
      </ul>
    </li>

    <li><span>Stage 4: Online Store 2.0</span>
      <ul class="tree">
        <li>Use JSON templates</li>
        <li>Implement dynamic sections and blocks</li>
      </ul>
    </li>

    <li><span>Stage 5: Shopify APIs</span>
      <ul class="tree">
        <li>Admin API (REST & GraphQL)</li>
        <li>Storefront API (GraphQL)</li>
        <li>Shopify Functions (custom logic)</li>
      </ul>
    </li>

    <li><span>Stage 6: App Development</span>
      <ul class="tree">
        <li>Understand App Types (Public, Custom)</li>
        <li>Use Shopify App CLI (Node.js, Remix, or Next.js)</li>
        <li>Use Polaris for UI</li>
        <li>Integrate Admin API</li>
      </ul>
    </li>

    <li><span>Stage 7: Advanced Topics</span>
      <ul class="tree">
        <li>Set up Webhooks</li>
        <li>Use App Bridge</li>
        <li>OAuth Authentication</li>
        <li>GraphQL Advanced Queries</li>
        <li>Billing API</li>
      </ul>
    </li>

    <li><span>Tools to Learn</span>
      <ul class="tree">
        <li>Shopify CLI</li>
        <li>Git / GitHub</li>
        <li>Postman / Insomnia</li>
        <li>Ngrok</li>
        <li>Theme Kit</li>
      </ul>
    </li>

    <li><span>Practice Projects</span>
      <ul class="tree">
        <li>Metafield-powered custom product page</li>
        <li>Advanced filterable theme</li>
        <li>Bulk product editor app</li>
        <li>Custom storefront using Storefront API + React</li>
        <li>Metaobject-driven FAQ section</li>
      </ul>
    </li>
  </ul>

</body>
</html>

    """
    try:
        browser = await launch(
            # This line tells pyppeteer where to find your browser
            executablePath=brave_executable_path,
            headless=True
        )
        page = await browser.newPage()
        await page.setContent(html_content)
        await page.screenshot({'path': 'shopify_roadmap_brave.png', 'fullPage': True})
        await browser.close()
        print("Image 'shopify_roadmap_brave.png' created successfully!")
    except FileNotFoundError:
        print(f"Error: Could not find Brave browser at the path specified.")
        print(f"Please check that the path '{brave_executable_path}' is correct.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())