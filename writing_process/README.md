# The Content Magic System (v2.0)

## Overview

This document outlines the **Content Magic System v2.0**, a refined multi-agent workflow for producing world-class, long-form SEO articles. This system is designed for deep collaboration between the user and a sophisticated LLM, which will adopt a series of expert personas at each stage of the content creation process. This version incorporates best practices from established multi-agent frameworks like MetaGPT and AutoGen, focusing on a more iterative and collaborative process.

## The Process

The system is an iterative workflow, managed by a master "Maestro" agent. It includes explicit checkpoints for user feedback and a "Round Table" critique session to ensure the highest quality output.

1.  **The Brief (User Input):** The process begins with the user providing a topic or a general idea for an article.

2.  **The Maestro (Project Kick-off):** The Maestro agent is activated. It reviews the user's brief, outlines the project plan, explains the workflow, and introduces the expert agent team.

3.  **The Investigator (Research):** The Research Agent gathers, analyzes, and synthesizes information about the topic. The output is a comprehensive research summary.

4.  **The Architect (Outlining):** The Outlining Agent crafts a detailed, SEO-optimized outline for the article.

5.  **USER CHECKPOINT #1: Outline Approval:** The Maestro presents the outline to the user for feedback and approval before proceeding.

6.  **The Storyteller (Writing):** The Writing Agent drafts the full article based on the approved outline.

7.  **USER CHECKPOINT #2: Draft Review:** The Maestro presents the first draft to the user for feedback and high-level revisions.

8.  **The Round Table (Critique and Refine):** The Investigator, Architect, and SEO Agent are re-activated to critique the draft from their specialized perspectives. This is a crucial step for iterative improvement.

9.  **The Guardian (Editing):** The Editing Agent performs a final, meticulous line-edit and fact-check.

10. **The Optimizer (SEO):** The SEO Agent performs a final optimization pass.

11. **Final Delivery:** The Maestro presents the completed, polished article to the user.

## The Agents

Each agent is a distinct persona with a specific role, defined in a separate `.md` file in this directory.

## The Goal

The goal of the Content Magic System v2.0 is to create a transparent, collaborative, and highly effective process for generating world-class, long-form content that consistently exceeds expectations.