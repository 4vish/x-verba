import openai

client = openai.OpenAI()


def test_case_1_ungoverned_ai_call(user_prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_prompt}],
    )
    send_to_user(response)
    return response


def test_case_2_agent_handover_with_validation(user_input):
    output_a = agent_a.run(user_input)
    if not validate(output_a):
        raise ValidationError("bad output")
    output_b = agent_b.run(output_a)
    return output_b


def test_case_3_dc_i11_detection(model_input):
    if model_confidence > 0.9:
        output = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": model_input}],
        )
        if output.confidence > threshold:
            approve(output)
    return output
