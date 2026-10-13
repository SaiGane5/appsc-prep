import React, { useState } from 'react';
import ContentRenderer from './ContentRenderer';
import MathText from './MathText';
import { 
  CheckCircle, 
  Circle, 
  Star, 
  Clock, 
  Printer, 
  ArrowLeft, 
  ArrowRight, 
  ChevronDown, 
  ChevronUp
} from 'lucide-react';

export default function TopicView({
  note,
  allNotes,
  onSelectTopic,
  isCompleted,
  onToggleComplete,
  isBookmarked,
  onToggleBookmark,
  onOpenImage,
  fontSizeMultiplier
}) {
  const [syllabusExpanded, setSyllabusExpanded] = useState(false);

  if (!note) {
    return (
      <div className="flex-1 flex items-center justify-center p-12 text-zinc-500">
        <p>Select a topic from the syllabus index to begin reading.</p>
      </div>
    );
  }

  // Find previous and next topics
  const currentIndex = allNotes.findIndex(n => n.topic_id === note.topic_id);
  const prevTopic = currentIndex > 0 ? allNotes[currentIndex - 1] : null;
  const nextTopic = currentIndex < allNotes.length - 1 ? allNotes[currentIndex + 1] : null;

  // Extract headings for quick table of contents
  const headings = note.content
    ?.filter(item => item.type === 'heading')
    ?.map((h, i) => ({
      text: h.text,
      level: h.level,
      id: `heading-${i}-${encodeURIComponent(h.text.slice(0, 24).replace(/\s+/g, '-'))}`
    })) || [];

  const handlePrint = () => {
    window.print();
  };

  return (
    <article className="flex-1 max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      {/* Top Meta Bar - Clean Monochrome */}
      <div className="flex flex-wrap items-center justify-between gap-3 pb-3 mb-6 border-b border-[#303036] text-xs">
        <div className="flex flex-wrap items-center gap-2 text-zinc-400">
          <span className="font-medium text-zinc-300">{note.subject_title}</span>
          <span className="text-zinc-600">•</span>
          <span>{note.paper}</span>
          <span className="text-zinc-600">•</span>
          <span className="flex items-center gap-1">
            <Clock size={12} className="text-zinc-400" /> {note.estimated_read_time_mins} min read
          </span>
          <span className="text-zinc-600 hidden sm:inline">•</span>
          <span className="hidden sm:inline">
            {note.word_count?.toLocaleString()} words
          </span>
        </div>

        {/* Minimal Action Controls */}
        <div className="flex items-center gap-2">
          <button
            onClick={() => onToggleBookmark(note.topic_id)}
            className={`flex items-center gap-1.5 px-2.5 py-1 rounded border text-xs font-medium transition-colors ${
              isBookmarked 
                ? 'bg-[#2a2a30] border-zinc-500 text-white' 
                : 'bg-[#222226] border-[#333338] text-zinc-400 hover:text-white hover:bg-[#28282e]'
            }`}
          >
            <Star size={12} fill={isBookmarked ? 'currentColor' : 'none'} />
            <span className="hidden sm:inline">{isBookmarked ? 'Saved' : 'Bookmark'}</span>
          </button>

          <button
            onClick={() => onToggleComplete(note.topic_id)}
            className={`flex items-center gap-1.5 px-2.5 py-1 rounded border text-xs font-medium transition-colors ${
              isCompleted 
                ? 'bg-[#2a2a30] border-zinc-500 text-white' 
                : 'bg-[#222226] border-[#333338] text-zinc-400 hover:text-white hover:bg-[#28282e]'
            }`}
          >
            {isCompleted ? <CheckCircle size={12} /> : <Circle size={12} />}
            <span className="hidden sm:inline">{isCompleted ? 'Completed' : 'Mark Done'}</span>
          </button>

          <button
            onClick={handlePrint}
            className="p-1 text-zinc-400 hover:text-white rounded bg-[#222226] border border-[#333338] hover:bg-[#28282e] transition-colors"
            title="Print or Save PDF"
          >
            <Printer size={13} />
          </button>
        </div>
      </div>

      {/* Main Title */}
      <header className="mb-6">
        <div className="text-[11px] font-mono text-zinc-500 uppercase tracking-wider mb-1.5">
          {note.topic_id}
        </div>
        <h1 className="text-2xl sm:text-3xl font-bold text-white tracking-tight leading-snug">
          <MathText text={note.topic_title} />
        </h1>
      </header>

      {/* Syllabus Mapping - Clean Understated Dropdown */}
      {note.syllabus_mapping && (
        <div className="mb-7 bg-[#212125] border border-[#303036] rounded-md overflow-hidden">
          <button
            onClick={() => setSyllabusExpanded(!syllabusExpanded)}
            className="w-full px-3.5 py-2 flex items-center justify-between text-left text-xs font-medium text-zinc-300 hover:text-white transition-colors"
          >
            <span>Syllabus Mapping: {note.syllabus_mapping.slice(0, 80)}...</span>
            <span className="text-zinc-400 shrink-0 ml-2">
              {syllabusExpanded ? <ChevronUp size={14} /> : <ChevronDown size={14} />}
            </span>
          </button>
          {syllabusExpanded && (
            <div className="px-3.5 py-2.5 text-xs text-zinc-300 leading-relaxed border-t border-[#2d2d33] bg-[#1a1a1d]">
              <MathText text={note.syllabus_mapping} />
            </div>
          )}
        </div>
      )}

      {/* Quick Navigation Anchors - Minimal Horizontal Bar */}
      {headings.length > 2 && (
        <div className="mb-8 p-3 bg-[#202024] border border-[#2e2e34] rounded-md">
          <div className="text-[11px] font-medium text-zinc-400 uppercase tracking-wide mb-2">
            Contents:
          </div>
          <div className="flex flex-wrap gap-1.5">
            {headings.filter(h => h.level <= 2).map((h, i) => (
              <a
                key={i}
                href={`#${h.id}`}
                className="text-xs px-2 py-0.5 rounded bg-[#27272c] text-zinc-300 hover:text-white hover:bg-[#323238] border border-[#333338] transition-colors truncate max-w-xs"
              >
                <MathText text={h.text} />
              </a>
            ))}
          </div>
        </div>
      )}

      {/* Body Content */}
      <main className="prose prose-invert max-w-none">
        <ContentRenderer 
          content={note.content} 
          onOpenImage={onOpenImage}
          fontSizeMultiplier={fontSizeMultiplier}
        />
      </main>

      {/* Bottom Prev / Next Nav - Minimal Monochrome */}
      <footer className="mt-14 pt-6 border-t border-[#303036] flex flex-col sm:flex-row items-center justify-between gap-4">
        {prevTopic ? (
          <button
            onClick={() => onSelectTopic(prevTopic.topic_id)}
            className="w-full sm:w-auto text-left p-3 rounded-lg bg-[#222226] border border-[#303036] hover:border-zinc-500 hover:bg-[#28282e] transition-colors group flex items-center gap-2.5"
          >
            <ArrowLeft size={14} className="text-zinc-400 group-hover:text-white transition-colors shrink-0" />
            <div className="min-w-0">
              <div className="text-[10px] uppercase text-zinc-500">Previous</div>
              <div className="text-xs font-medium text-zinc-200 group-hover:text-white truncate max-w-xs">{prevTopic.topic_title}</div>
            </div>
          </button>
        ) : <div />}

        {nextTopic && (
          <button
            onClick={() => onSelectTopic(nextTopic.topic_id)}
            className="w-full sm:w-auto text-right p-3 rounded-lg bg-[#222226] border border-[#303036] hover:border-zinc-500 hover:bg-[#28282e] transition-colors group flex items-center justify-end gap-2.5"
          >
            <div className="min-w-0">
              <div className="text-[10px] uppercase text-zinc-500">Next</div>
              <div className="text-xs font-medium text-zinc-200 group-hover:text-white truncate max-w-xs">{nextTopic.topic_title}</div>
            </div>
            <ArrowRight size={14} className="text-zinc-400 group-hover:text-white transition-colors shrink-0" />
          </button>
        )}
      </footer>
    </article>
  );
}
