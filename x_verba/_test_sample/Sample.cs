using OpenAI.Chat;

namespace AgentApp
{
    public class AgentRunner
    {
        public async Task<string> RunAgent(string input, string mode)
        {
            bool isValid = ValidateInput(input);
            if (!isValid)
            {
                throw new Exception("invalid input");
            }
            else if (mode == "fast")
            {
                Console.WriteLine("fast mode");
            }

            string label = isValid ? "ok" : "bad";

            switch (mode)
            {
                case "fast":
                    DoFastThing();
                    break;
                case "slow":
                    DoSlowThing();
                    break;
                default:
                    DoDefaultThing();
                    break;
            }

            foreach (var item in new[] { 1, 2, 3 })
            {
                Console.WriteLine(item);
            }

            try
            {
                await FetchDataAsync(input);
            }
            catch (Exception)
            {
            }

            try
            {
                Db.Delete(input);
            }
            catch (Exception e)
            {
                Logger.Error("delete failed", e);
                NotifyAdmin(e);
            }

            if (RequireApproval(input))
            {
                await Agent.InvokeAsync(input);
            }

            var client = new OpenAIClient("sk-test");
            var chatClient = client.GetChatClient("gpt-4");
            var result = await chatClient.CompleteChatAsync(input);

            return result.ToString();
        }
    }
}
