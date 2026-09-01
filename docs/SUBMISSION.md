# GenLayer Builder Submission Checklist

## Before you submit

- [ ] Create a public GitHub repository named `genlayer-contract-verify`.
- [ ] Push the repository root, including `README.md`, `contracts/contract_verify.py`, `src/`, and this checklist.
- [ ] Open the app and confirm the first screen loads on desktop and mobile.
- [ ] Connect a test wallet and confirm the account and chain ID appear.
- [ ] Enter a valid EVM address and confirm invalid addresses are rejected.
- [ ] Run the read-only check and confirm its result is clearly labeled.
- [ ] Click **Simulate transaction** and confirm the four states complete without a wallet signature.
- [ ] Open `contracts/contract_verify.py` in GenLayer Studio and deploy it in the local Studio environment.
- [ ] Call `verify_from_page` with the address, a public explorer/contract page URL, and network name.
- [ ] Confirm the Studio execution reaches consensus on the page check.
- [ ] Optionally call `record_verification` with the same address/network/result shown in the browser preflight.
- [ ] Call `latest_verification` and confirm the stored snapshot is returned.

## Recommended submission text

### One-line summary

GenLayer Contract Verify is a wallet-aware preflight desk that helps builders validate an EVM contract address and understand the transaction lifecycle before they interact with an Intelligent Contract.

### What makes it useful

Contract interactions often fail because the address, network, or wallet context is unclear. This project turns that first check into a small, readable workflow and separates read-only inspection from a visual demo state.

### GenLayer component

The included `ContractVerifier` Intelligent Contract stores the latest verification snapshot in GenLayer Studio and exposes it through a read-only method. It is intentionally small and transparent so a reviewer can run it quickly.

## Important disclosure

The browser demo transaction is simulated. It does not sign, broadcast, or move funds. The GenLayer Studio method is a separate contract interaction used to demonstrate state recording in the local Studio environment. If the UI is later connected to a real RPC or deployed contract, update the copy and verification behavior together.

## Links to provide

- Live demo: add the published app URL.
- GitHub: add the public repository URL.
- Studio contract: point reviewers to `contracts/contract_verify.py`.