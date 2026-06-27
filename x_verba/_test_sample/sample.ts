import { generateText } from "ai";

interface Options {
  retries?: number;
  mode?: "fast" | "slow";
}

export async function runAgent(input: string, opts: Options = {}) {
  const isValid = validateInput(input);
  if (!isValid) {
    throw new Error("invalid input");
  } else if (opts.mode === "fast") {
    console.log("fast mode");
  }

  const label = isValid ? "ok" : "bad";

  switch (opts.mode) {
    case "fast":
      doFastThing();
      break;
    case "slow":
      doSlowThing();
      break;
    default:
      doDefaultThing();
  }

  for (const item of [1, 2, 3]) {
    console.log(item);
  }

  try {
    await fetch("https://api.example.com/data", { method: "POST" });
  } catch (err) {
    // swallow error silently
  }

  try {
    db.delete(input);
  } catch (e) {
    console.error("delete failed", e);
    notifyAdmin(e);
  }

  if (requireApproval(input)) {
    await agent.invoke(input);
  }

  const result = await generateText({ prompt: input });
  return result;
}
