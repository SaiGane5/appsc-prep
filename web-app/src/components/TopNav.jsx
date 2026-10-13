import React from 'react';
import { 
  Menu, 
  BookOpen, 
  HelpCircle, 
  FileText, 
  BarChart3
} from 'lucide-react';

export default function TopNav({
  viewMode,
  setViewMode,
  fontSizeMultiplier,
  setFontSizeMultiplier,
  totalBookmarksCount,
  onToggleSidebar
}) {
  const modes = [
    { id: 'notes', label: 'Notes', icon: BookOpen },
    { id: 'mcqs', label: 'Practice MCQs', icon: HelpCircle },
    { id: 'mains', label: 'Mains Bank', icon: FileText },
    { id: 'dashboard', label: 'Progress', icon: BarChart3 }
  ];

  return (
    <header className="h-13 shrink-0 bg-[#18181b] border-b border-[#303036] px-3 sm:px-5 flex items-center justify-between z-30">
      {/* Left: Sidebar Toggle & Minimal Branding */}
      <div className="flex items-center gap-3">
        <button
          onClick={onToggleSidebar}
          className="p-1.5 text-zinc-400 hover:text-white rounded-md hover:bg-[#26262b] transition-colors"
          title="Toggle Syllabus Sidebar"
        >
          <Menu size={18} />
        </button>

        <div className="flex items-center gap-2">
          <span className="font-semibold text-sm sm:text-base tracking-tight text-white whitespace-nowrap">
            APPSC Group-1
          </span>
          <span className="text-[11px] text-zinc-500 hidden md:inline">
            Syllabus & Question Bank
          </span>
        </div>
      </div>

      {/* Center: Monochromatic Mode Tabs */}
      <nav className="flex items-center gap-1 bg-[#202024] p-1 rounded-lg border border-[#303036]">
        {modes.map(mode => {
          const Icon = mode.icon;
          const isActive = viewMode === mode.id;
          return (
            <button
              key={mode.id}
              onClick={() => setViewMode(mode.id)}
              className={`
                flex items-center gap-1.5 px-3 py-1 rounded-md text-xs font-medium transition-colors
                ${isActive 
                  ? 'bg-[#2e2e34] text-white border border-[#44444c]' 
                  : 'text-zinc-400 hover:text-zinc-200 hover:bg-[#26262b] border border-transparent'}
              `}
            >
              <Icon size={13} className="shrink-0" />
              <span>{mode.label}</span>
            </button>
          );
        })}
      </nav>

      {/* Right: Text Size Control */}
      <div className="flex items-center gap-2">
        <div className="flex items-center gap-1 bg-[#202024] border border-[#303036] rounded-md p-0.5 text-xs text-zinc-400">
          <button
            onClick={() => setFontSizeMultiplier(prev => Math.max(0.85, prev - 0.08))}
            className="px-2 py-0.5 hover:text-white hover:bg-[#28282e] rounded transition-colors font-mono"
            title="Decrease font size"
          >
            A-
          </button>
          <button
            onClick={() => setFontSizeMultiplier(1)}
            className="px-1.5 py-0.5 hover:text-white hover:bg-[#28282e] rounded transition-colors font-mono text-[11px]"
            title="Reset font size"
          >
            100%
          </button>
          <button
            onClick={() => setFontSizeMultiplier(prev => Math.min(1.35, prev + 0.08))}
            className="px-2 py-0.5 hover:text-white hover:bg-[#28282e] rounded transition-colors font-mono"
            title="Increase font size"
          >
            A+
          </button>
        </div>
      </div>
    </header>
  );
}
