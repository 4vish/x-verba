package agent

import (
	"context"
	"fmt"

	"github.com/sashabaranov/go-openai"
)

func RunAgent(ctx context.Context, input string, mode string) (string, error) {
	isValid := validateInput(input)
	if !isValid {
		return "", fmt.Errorf("invalid input")
	} else if mode == "fast" {
		fmt.Println("fast mode")
	}

	switch mode {
	case "fast":
		doFastThing()
	case "slow":
		doSlowThing()
	default:
		doDefaultThing()
	}

	for i := 0; i < 3; i++ {
		fmt.Println(i)
	}

	result, err := fetchData(ctx, input)
	if err != nil {
		return "", err
	}

	data, err := db.Delete(input)
	if err != nil {
		log.Error("delete failed", err)
		notifyAdmin(err)
	}

	if requireApproval(input) {
		agent.Invoke(input)
	}

	client := openai.NewClient("sk-test")
	resp, err := client.CreateChatCompletion(ctx, openai.ChatCompletionRequest{
		Model:       "gpt-4",
		Temperature: 0.7,
		MaxTokens:   500,
	})
	if err != nil {
		return "", err
	}

	return resp.Choices[0].Message.Content, nil
}
