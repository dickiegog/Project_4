document.addEventListener("DOMContentLoaded", function() {
    const editButtons = document.getElementsByClassName("btn-edit");
    const commentText = document.getElementById("id_body");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");
  
    console.log(editButtons);  // Confirm buttons are loaded
  
    Array.from(editButtons).forEach(button => {
      button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
  
        if (commentText && commentForm) {
          commentText.value = commentContent;
          submitButton.innerText = "Update";
          commentForm.setAttribute("action", `edit_comment/${commentId}`);
          console.log(`edit_comment/${commentId}`);
        } else {
          console.log("Comment form or text area not found");
        }
      });
    });
  
    // Delete button handling
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteConfirm = document.getElementById("deleteConfirm");
  
    Array.from(deleteButtons).forEach(button => {
      button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        deleteConfirm.href = `delete_comment/${commentId}/`;
        deleteModal.show();
      });
    });
  });
