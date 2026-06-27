use async_openai::Client;

fn run_agent(input: &str, mode: &str) -> String {
    let is_valid = validate_input(input);
    if !is_valid {
        panic!("invalid input");
    } else if mode == "fast" {
        println!("fast mode");
    }

    match mode {
        "fast" => do_fast_thing(),
        "slow" => do_slow_thing(),
        _ => do_default_thing(),
    }

    for item in 0..3 {
        println!("{}", item);
    }

    let data = fetch_data(input).unwrap();

    let result = db_delete(input).expect("delete failed");

    if require_approval(input) {
        agent.invoke(input);
    }

    let client = Client::new();
    let response = client.chat().create(request).unwrap();

    response
}
