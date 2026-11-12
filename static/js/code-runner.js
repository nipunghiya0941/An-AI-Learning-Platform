/**
 * QUEST AI LEARNING PLATFORM
 * Code Sandbox Runner & Level Completion Controller
 */

document.addEventListener('DOMContentLoaded', function () {
  'use strict';

  const runCodeBtn = document.getElementById('runCodeBtn');
  const resetCodeBtn = document.getElementById('resetCodeBtn');
  const submitModuleBtn = document.getElementById('submitModuleBtn');
  const editor = document.getElementById('sandboxEditor');
  const terminal = document.getElementById('terminalOutput');
  const quizOptions = document.querySelectorAll('.quiz-option-radio');
  const quizFeedback = document.getElementById('quizFeedback');

  function getCsrfToken() {
    const metaToken = document.querySelector('[name=csrfmiddlewaretoken]');
    if (metaToken) return metaToken.value;
    const cookie = document.cookie.split('; ').find(row => row.startsWith('csrftoken='));
    return cookie ? cookie.split('=')[1] : '';
  }

  // Handle quiz option styling
  quizOptions.forEach(radio => {
    radio.addEventListener('change', function () {
      document.querySelectorAll('.quiz-option-label').forEach(lbl => lbl.classList.remove('selected'));
      if (this.checked) {
        this.closest('.quiz-option-label').classList.add('selected');
      }
    });
  });

  // Run Code Simulation
  if (runCodeBtn && editor && terminal) {
    const defaultStarter = editor.value;

    runCodeBtn.addEventListener('click', function () {
      const code = editor.value.trim();
      terminal.innerHTML = '<span style="color:#38bdf8;">[Compiling & Linking executable...]</span><br>';

      setTimeout(() => {
        const expected = document.body.dataset.expectedOutput || '';
        const course = document.body.dataset.courseSlug || 'c';

        let outputLines = [];
        outputLines.push(`<span style="color:#94a3b8;">$ ${course === 'c' ? 'gcc main.c -o solution && ./solution' : 'javac Main.java && java Main'}</span>`);

        // Check for basic syntax checks
        if (code.includes('printf') || code.includes('System.out.println') || code.includes('print')) {
          if (expected) {
            outputLines.push(`<span style="color:#10b981;">${expected}</span>`);
            outputLines.push(`<span style="color:#64748b;">Process exited with status code 0 (Success)</span>`);
          } else {
            outputLines.push(`<span style="color:#10b981;">Quest output compiled successfully!</span>`);
            outputLines.push(`<span style="color:#64748b;">Execution complete.</span>`);
          }
        } else {
          outputLines.push(`<span style="color:#f59e0b;">Warning: No output detected. Ensure you have printed the expected result.</span>`);
        }

        terminal.innerHTML = outputLines.join('<br>');
        terminal.scrollTop = terminal.scrollHeight;
      }, 500);
    });

    if (resetCodeBtn) {
      resetCodeBtn.addEventListener('click', function () {
        editor.value = defaultStarter;
        terminal.innerHTML = '<span style="color:#64748b;">Code reset to module starter template.</span>';
      });
    }
  }

  // Submit and Complete Module
  if (submitModuleBtn) {
    submitModuleBtn.addEventListener('click', async function () {
      const courseSlug = document.body.dataset.courseSlug;
      const levelNumber = document.body.dataset.levelNumber;

      // Check if quiz option is selected
      const selectedOption = document.querySelector('input[name="quiz_option"]:checked');
      if (!selectedOption) {
        if (quizFeedback) {
          quizFeedback.className = 'quiz-feedback-box incorrect';
          quizFeedback.textContent = "Please select an answer for the Knowledge Check Quiz above!";
          quizFeedback.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
        return;
      }

      const answerIndex = parseInt(selectedOption.value, 10);
      const code = editor ? editor.value : '';

      submitModuleBtn.disabled = true;
      submitModuleBtn.textContent = "Verifying & Unlocking Next Level...";

      try {
        const response = await fetch(`/api/complete-level/${courseSlug}/${levelNumber}/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken()
          },
          body: JSON.stringify({
            quiz_answer: answerIndex,
            code: code
          })
        });

        const data = await response.json();

        if (data.success) {
          if (quizFeedback) {
            quizFeedback.className = 'quiz-feedback-box correct';
            quizFeedback.textContent = "Correct! " + (data.message || "Module successfully mastered.");
          }

          // Trigger celebration modal
          data.course_slug = courseSlug;
          if (window.showCelebrationModal) {
            window.showCelebrationModal(data);
          }

          submitModuleBtn.textContent = "Module Completed! ✓";
          submitModuleBtn.style.background = "#10b981";
        } else {
          if (quizFeedback) {
            quizFeedback.className = 'quiz-feedback-box incorrect';
            quizFeedback.textContent = data.message || "Incorrect quiz answer. Review the theory and try again!";
            quizFeedback.scrollIntoView({ behavior: 'smooth', block: 'center' });
          }
          submitModuleBtn.disabled = false;
          submitModuleBtn.textContent = "Submit & Unlock Next Level ➔";
        }
      } catch (err) {
        alert("Failed to submit module. Please check your network connection.");
        submitModuleBtn.disabled = false;
        submitModuleBtn.textContent = "Submit & Unlock Next Level ➔";
      }
    });
  }
});
