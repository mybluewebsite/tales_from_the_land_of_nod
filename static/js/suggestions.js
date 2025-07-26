const editButtons = document.getElementsByClassName("btn-edit");
const suggestionText = document.getElementById("id_body");
const suggestionForm = document.getElementById("suggestionForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

// Add event listeners to all edit buttons
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let suggestionId = e.target.getAttribute("suggestion_id");
    let suggestionContent = document.getElementById(`suggestion${suggestionId}`).innerText;
    suggestionText.value = suggestionContent.trim();
    submitButton.innerText = "Update";
    suggestionForm.setAttribute("action", `edit_suggestion/${suggestionId}/`);
  });
}

// Add event listeners to all delete buttons
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let suggestionId = e.target.getAttribute("suggestion_id");
    deleteConfirm.href = `delete_suggestion/${suggestionId}/`;
    deleteModal.show();
  });
}