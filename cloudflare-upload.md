# Cloudflare Pages deploy instructions for the assayer article

Give this to the browser agent along with the Cloudflare account login. The article is already built on the laptop at `C:\Users\alexk\projects\acokovaceski\deploy\root`. The only thing missing is a deploy credential with the Pages permission.

## Option A: create a Pages-scoped API token (preferred)

1. Go to https://dash.cloudflare.com and log in with Aco's account.
2. Profile (top right) -> API Tokens -> Create Token.
3. Choose the **"Edit Cloudflare Pages"** template if it is listed. Otherwise create a custom token with permission **Account -> Cloudflare Pages -> Edit**, on the account (or on the zone acokovaceski.com if it asks for a zone).
4. Create the token and copy it.
5. On the laptop, in `C:\Users\alexk\projects\acokovaceski`, run in PowerShell:

   ```powershell
   $env:CLOUDFLARE_API_TOKEN = "<the new token>"
   npx wrangler pages deploy deploy/root --project-name acokovaceski --branch main
   ```

6. Verify https://acokovaceski.com/writing/the-assayer.html loads and shows "The assayer" by Aco Kovaceski, dated 24 November 2026, with the verified receipt and the independent corroboration by Michael Rubinstein.

## Option B: OAuth login (if a token cannot be created)

1. On the laptop, in the same directory:

   ```powershell
   Remove-Item Env:CLOUDFLARE_API_TOKEN
   npx wrangler login
   ```

2. A browser opens for Cloudflare OAuth. Authorise it and wait for the terminal to confirm the login.
3. Then run:

   ```powershell
   npx wrangler pages deploy deploy/root --project-name acokovaceski --branch main
   ```

4. Verify the same URL as above.

## Notes

- The token currently set on the laptop lacks the Pages scope; that is why deploys failed with code 10000. Do not reuse it.
- The stored OAuth credential on the laptop expired on 11 November, so a fresh login is needed if going the OAuth route.
- The article is already built and committed in the site's git. Only the deploy is missing.
