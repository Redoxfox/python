
  function Validate(field, regex) {
    valid = true;
    if(field.match(regex) == null) {
      valid = false;
    }
    return valid;
  }

  function ValidateForm() {
    username = document.querySelectorAll('[fs-field-validation-name="Gitlab Username"]')[0].getElementsByTagName('input')[0].value;
    user_regex = /^[a-z0-9]{1,12}$/;
    user_valid = Validate(username, user_regex);

    text = document.querySelectorAll('[fs-field-validation-name="Repo Access Message"]')[0].getElementsByTagName('textarea')[0].value;
    repo = document.querySelectorAll('[fs-field-validation-name="Repo"]')[0].getElementsByTagName('select')[0].value;
    if(repo == "Challenges") {
      text_regex = /I have read and understood all documentation pertaining to technical challenges, I agree to all of the terms and therefore request access to the git Challenges repository with my GitLab username/;
    }
    else {
      text_regex = /I have completed three \(3\) programming and three \(3\) ctf-hacking unique challenges in the training repo and therefore request access to the git writeups repository with my GitLab username/;
    }
    text_valid = Validate(text, text_regex);

    form_valid = true;
    alert_message = "";
    if(!user_valid) {
      alert_message += "\nYour username must be at most 12 characters long and have only lowercase letters and numbers.";
      form_valid = false;
    }
    if(!text_valid) {
      alert_message += "\n\nPaste the correct message.";
      form_valid = false;
    }

    if(!form_valid) {
      window.alert(alert_message);
    }
    return form_valid;
  }


  form = document.forms[0];
  form.setAttribute('onsubmit', 'return ValidateForm()');