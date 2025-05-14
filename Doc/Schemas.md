# Overview

### Common Definitions

**Prompt**: a single request from Idle Hands to the LLM.

**Response**: a single response from the LLM.

**Interaction**: a single Idle Hands prompt and its associated LLM response.

**Conversation**: the set of associated interactions initiated from a single request.

**The Client**: the Idle Hands instance. Because it's easier to refer to it as such in technical documentation.

**Action**: a Python function that the LLM can invoke via a response.

---

### "Conversation" Flow

Idle Hands interfaces with the configured API by simulating conversational prompts and processing the LLM's response. Every interaction is initiated by the client, never by the LLM. Depending on the LLM's response, the client may initiate subsequent interactions to produce multi-interaction conversations.

Conversations typically end with either a `Basic` response or an `Perform Action` response, but this is not strictly required.

---

### Context

For the LLM to respond appropriately, each request must identify the client's capabilities and should provide instructions for how to structure its response.

To minimize the size of each request (consequently minimizing API tokens), Idle Hands only includes context necessary to produce an immediate response. If the LLM attempts to perform an action that requires information specific to that action, it can produce a "more context" response targeting that specific action.

**global_context.yaml** provides text that is included in all conversations. This includes basic interaction rules and personality information.

**action_context.yaml** provides action-specific context that should only be included when required.

---


Below are the basic requests and responses that are included in the global context.

### Request Types

* **Routine Check-In**
    - Provides monitored data to the LLM. This is how the LLM knows what you're doing with your life.

* **Image Prompt Echo**
    - When the LLM suggests an image generation prompt via `Image Prompt`, the client must submit it back to the LLM as a separate prompt.

* **Provide Context**
    - When the LLM requires additional context for a specific action, this request type is used to provide additional details.

* **Action Execution Details**
    - This request type is used to both report the outcome of executed actions and allow the LLM to provide a follow-up response.



### Response Types

* **Basic Response**
    - Provides conversational text to the client.
* **Request Context**
    - The response type used to request additinal context about a specific action.
* **Image Prompt**
    - When the LLM wants to generate an image, it uses this response type to return the image generation prompt to the client, which can be used for the `Image Prompt Echo` request.
* **Image URL**
    - The response type used to return a generated image to the client.
* **Perform Action**
    - The response type used to instruct the client to execute a local action.

### Actions

As an "accountability panopticon", Idle Hands must provide a means for the LLM to directly influence the user's life in the event of their eventual failure. This feature is realized through **Actions**: arbitrary Python functions that the LLM can execute without consulting the user.

The "Perform Action" response provides instructions to the client to invoke pre-defined functions with specified paramters. For example, the `create_file` action may be defined that allows the LLM to generate a file on the user's filesystem. Or the `delete_file` action may allow it to ruin your day if you upset it. The `jumpscare` action can be a lot of fun if the LLM prefaces it with the `adjust_volume` action.

There's also an `eval` action, disabled by default. Feel free to enable it if you're feeling brave enough.

I must reiterate that I take no responsibility for any damages.