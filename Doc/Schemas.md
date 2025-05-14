# Schemas

### Common Definitions

**Prompt**: a single request from Idle Hands to the LLM.

**Response**: a single response from the LLM.

**Interaction**: a single Idle Hands prompt and its associated LLM response.

**Conversation**: the set of associated interactions initiated from a single request.

**The Client**: the Idle Hands instance

---

### "Conversation" Flow

Idle Hands interfaces with the configured API by simulating conversational prompts and processing the LLM's response. The client

---

### Context

For the LLM to respond appropriately, each request must identify the client's capabilities and should provide instructions for how to structure its response.

To minimize the size of each request (consequently minimizing API tokens), Idle Hands only includes context necessary to produce an immediate response. If the LLM attempts to perform an action that requires information specific to that action, it can produce a "more context" response targeting that specific action.

**global_context.yaml** provides text that is included in all conversations. This includes basic interaction rules and personality information.

**action_context.yaml** provides action-specific context that should only be included when required.

---

### Request Schemas


### Response Schemas